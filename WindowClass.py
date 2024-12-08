from tkinter import *
from tkmacosx import Button

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.resizable(False, False)
        self.window.configure(bg="white")
        self.window.title('BriKet')

    def openWindow(self):
        self.window.mainloop()

    def closeWindow(self):
        self.window.destroy()



