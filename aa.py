import win32api, win32gui, time, numpy

correct = [234, 65, 65]
defusetime = 40

while True:    
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower() == "counter-strike: global offensive":
        window_id = win32gui.GetDesktopWindow()
        window_dc = win32gui.GetWindowDC(window_id)
        long_colour = win32gui.GetPixel(window_dc, 929, 788)
        colour = int(long_colour)
        full = [(colour & 0xff),  ((colour >> 8) & 0xff), ((colour >> 16) & 0xff)]
        if numpy.array_equal(full, correct):
            print("planted")
            break

while True:
    defusetime -= 0.01
    print(defusetime)
    time.sleep(0.01)