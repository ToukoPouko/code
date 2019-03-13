import win32api, win32gui, time, datetime
'''while True:
    window_id = win32gui.GetDesktopWindow()
    window_dc = win32gui.GetWindowDC(window_id)
    long_colour = win32gui.GetPixel(window_dc, )
    colour = int(long_colour)
    print((colour & 0xff),  ((colour >> 8) & 0xff), ((colour >> 16) & 0xff))'''

'''while True:
    print(win32gui.GetCursorPos())
    time.sleep(1)   '''

start_time = time.time()

while True:
    print(40 + (start_time - time.time()))

