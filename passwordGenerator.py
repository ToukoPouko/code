import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.textbox = tk.Entry(self)
        self.choice1 = tk.Checkbutton(self)
        self.textbox.pack()
        self.choice1.pack()
            

root = tk.Tk()
app = Application(master=root)
app.mainloop()
