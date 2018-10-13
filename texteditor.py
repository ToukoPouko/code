import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.textbox = tk.Entry(self).grid(sticky='nsew')
        self.textbox.pack()


root = tk.Tk()
root.resizable(width=True, height=True)
root.geometry('{}x{}'.format(500, 500))
app = Application(master=root)
app.mainloop()
