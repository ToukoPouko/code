import win32gui, time, numpy, pyautogui, sys
from tkinter import *



window = Tk()
window.title("Bomba Timer")
window.geometry("300x300")


lblTime = Label(window, text="40.000")
lblTime.grid(column=1, row=1)

window.mainloop()

correct = [234, 65, 65]
defusetime = 39.89999


def check():
    global start_time
    while True:    
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower() == "counter-strike: global offensive":
            window_id = win32gui.GetDesktopWindow()
            window_dc = win32gui.GetWindowDC(window_id)
            long_colour = win32gui.GetPixel(window_dc, 671, 759)
            colour = int(long_colour)
            full = [(colour & 0xff),  ((colour >> 8) & 0xff), ((colour >> 16) & 0xff)]
            if numpy.array_equal(full, correct):
                print("planted")
                start_time = time.time()
                break
    timer()


def timer():
    while True:
        current_time = 40 + (start_time - time.time())
        sys.stdout.flush()
        print(round(current_time, 5))
        lblTime.configure(text=str(round(current_time, 2)))
        if current_time <= 0:
            break
    check()

if __name__ == "__main__":
    check()