from desktopmagic.screengrab_win32 import saveRectToBmp
import time
from datetime import datetime


while True:
    print("60 seconds until next")
    time.sleep(60)
    currTime = datetime.now().time()
    fixed = str(currTime).replace(":", "")
    saveRectToBmp("Screenshot" + str(fixed) + ".png", rect=(-690,-40,-150,260))
    print("Screenshot taken")