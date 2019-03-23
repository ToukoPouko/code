from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import *
from tkinter.messagebox import *
import os, io


class MyApp(Frame):
    def __init__(self, master, *args, **kwargs):
        
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master 

        self.master.title("Untitled - Notebad")

        self.defaultdir = "/"

        self.toolbar = Frame(self.master, bg="#eee")
        self.toolbar.pack(side="top", fill="both")

        '''self.btnBold = Button(self.toolbar, text="Bold", command=self.make_bold)
        self.btnBold.pack(side="left")    

        self.bold_font = Font(family="Times New Roman", size=12, weight="bold")  (bold)'''

        self.normal_font = Font(family="Linux Biolinum G", size=13)  

        self.text = Text(self.master, font=self.normal_font, background="#212121", foreground="lightgreen", insertbackground="lightgreen")
        self.text.focus()
        self.text.pack(fill="both", expand=True) 

        self.file = None
        
        self.fileList = [""]

        self.var = StringVar(self.master)
        self.var.set(self.fileList[0])
        self.var.trace("w", self.openFileCurrentDir)

        

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="New", command=self.newFile)
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Open Directory", command=self.openDir)
        file.add_command(label="Save", command=self.saveFile)       
        file.add_command(label="Exit", command=self.window_exit)

        menu.add_cascade(label="File", menu=file)

    def newFile(self):
        self.saveFile()
        self.master.title("Untitled - Notebad")
        self.file = None
        self.text.delete("1.0", "end")

    def openDir(self):
        self.defaultdir = askdirectory()
        if self.defaultdir == "":
            self.defaultdir = "/"

        for f in os.listdir(self.defaultdir):
            if f.endswith(".txt"):
                self.fileList.append(self.defaultdir + "/" + f)
                print(f)
        
        self.fileOptionMenu = OptionMenu(self.master, self.var, *self.fileList)
        self.fileOptionMenu.pack()

        self.updateOm()

    def updateOm(self):
        menu = self.fileOptionMenu["menu"]
        menu.delete(0, "end")

        for item in self.fileList:
            menu.add_command(label=item, command=lambda value=item: self.var.set(value))

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])

        if self.file == "":
            self.file = None
        else:        
            self.text.delete("1.0", "end")

            try:
                with io.open(self.file, "r", encoding="utf8") as file:
                    self.text.insert("1.0", file.read())
                    self.master.title(os.path.basename(self.file) + " - Notebad")
            except:
                self.file = None
                

    def openFileCurrentDir(self, *args):
        print(self.var.get())
        self.text.delete("1.0", "end")
        self.file = self.var.get()

        try:
            with io.open(self.file, "r", encoding="utf8") as file:
                    self.text.insert("1.0", file.read())
                    self.master.title(os.path.basename(self.file) + " - Notebad")
        except:
            self.file = None



    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(defaultextension = ".txt", initialdir = self.defaultdir, title = "Select file", filetypes = [("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.file != "":
            with io.open(self.file, "w", encoding = "utf8") as file:
                file.write(self.text.get("1.0", "end"))
                self.master.title(os.path.basename(self.file) + " - Notebad")
        elif self.file == "":
            self.file = None
            


    def window_exit(self):
        self.master.quit()
        
def main():
    root = Tk()
    root.configure
    root.geometry("500x500")

    app = MyApp(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()