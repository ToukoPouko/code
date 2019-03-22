from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import *
from tkinter.messagebox import *
import os


class MyApp(Frame):
    def __init__(self, master, *args, **kwargs):
        
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master 

        self.master.title("Untitled - Notebad")

        self.toolbar = Frame(self.master, bg="#eee")
        self.toolbar.pack(side="top", fill="both")

        '''self.btnBold = Button(self.toolbar, text="Bold", command=self.make_bold)
        self.btnBold.pack(side="left")    

        self.bold_font = Font(family="Times New Roman", size=12, weight="bold")  (bold)'''

        self.normal_font = Font(family="Linux Biolinum G", size=13)  

        self.text = Text(self.master, font=self.normal_font, background="#212121", foreground="lightgreen", insertbackground="lightgreen")
        self.text.focus()
        self.text.pack(fill="both", expand=True)

        #self.text.tag_configure("BOLD", font=self.bold_font)

        #self.btnCheckTags = Button(self.toolbar, text="Check Tags", command=self.check_tags)
        #self.btnCheckTags.pack(side="left")

        self.file = None

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="New File", command=self.newFile)
        file.add_command(label="Open File", command=self.openFile)
        file.add_command(label="Save File", command=self.saveFile)       
        file.add_command(label="Exit", command=self.window_exit)

        menu.add_cascade(label="File", menu=file)

    def newFile(self):
        '''if self.file != None:
            self.saveFile()
        elif self.file == None:
            self.master.title("Untitled - Notebad")
            self.file = None
            self.text.delete("1.0", "end")'''
        self.master.title("Untitled - Notebad")
        self.file = None
        self.text.delete("1.0", "end")

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.master.title(os.path.basename(self.file) + " - Notebad")
            self.text.delete("1.0", "end")

            file = open(self.file, "r")

            self.text.insert("1.0", file.read())

            file.close()

    def saveFile(self):
        return

    def make_bold(self):  
        try:
            if "BOLD" in self.text.tag_names():
                print("yeet1")
                self.text.tag_remove("BOLD", "1.0", "end")
            elif not "BOLD" in self.text.tag_names():
                self.text.tag_add("BOLD", "sel.first", "sel.last")
                print("yeet2")
        except TclError:
            pass

    def check_tags(self):
        print(self.text.tag_names("BOLD"))

    def window_exit(self):
        exit()
        
def main():
    root = Tk()
    root.configure
    root.geometry("500x500")

    app = MyApp(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()