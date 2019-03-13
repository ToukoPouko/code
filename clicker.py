import tkinter as tk
import win32api


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.pack_propagate(0)
        
        self.create_widgets()
        

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command = self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

state_down = win32api.GetKeyState(0x01)

'''while True:
    state = win32api.GetKeyState(0x01)
    if state != state_down:
        break
'''
root = tk.Tk()
app = Application(master=root)
app.mainloop()