import win32api, time, win32clipboard
from desktopmagic.screengrab_win32 import saveRectToBmp
from datetime import datetime
from io import BytesIO
from PIL import Image

state = win32api.GetKeyState(0x01)
firstPos = 0
secPos = None

def set_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()



def take_screenshot():
    if firstPos[0] <= secPos[0]:
        x1 = secPos[0]
        x2 = firstPos[0]
    else:
        x1 = firstPos[0]
        x2 = secPos[0]

    if firstPos[1] >= secPos[1]:
        y1 = secPos[1]
        y2 = firstPos[1]
    else:
        y1 = firstPos[1]
        y2 = secPos[1]

    currTime = datetime.now().time()
    fixed = str(currTime).replace(":", "")
    filename = "Screenshot" + str(fixed) + ".png"
    #saveRectToBmp(filename, rect=(firstPos[0], firstPos[1], secPos[0], secPos[1]))
    saveRectToBmp(filename, rect=(x1, y1, x2, y2))
    print("Screenshot taken")
    copy_to_clipboard(filename)


def copy_to_clipboard(filepath):
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    set_clipboard(win32clipboard.CF_DIB, data)


while True:
    a = win32api.GetKeyState(0x01)

    if a != state:
        state = a
        print(a)
        if a < 0:
            print("Left button pressed")
            if firstPos != 0:
                secPos = win32api.GetCursorPos()
                print(secPos)
                break
            else:
                firstPos = win32api.GetCursorPos()
                print(firstPos)


take_screenshot()
#Okay
