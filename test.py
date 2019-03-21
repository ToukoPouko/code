import tkinter as tk
import time

class Application:

    def __init__(self, master):
        self.master = master
        master.title("Test")

        self.label = Label(master, text="0")

