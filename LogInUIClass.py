from tkinter import *
from tkmacosx import Button

class LogIn:
    def __init__(self, window):
        self.window = window.window
        self.topText = Label(self.window, text="Authorization",
                        font=("Arial", 80), fg="black", bg="white")
        self.userNameEntry = Entry(self.window, width=24, fg="white", bg='black', font=("Arial", 30))
        self.passwordEntry = Entry(self.window, width=24, fg="white", bg='black', font=("Arial", 30))
        self.confirmButton = Button(self.window, text="Confirm", height=60, width=300, fg="white", bg='black', font=("Arial", 32, 'bold'), command=lambda:self.switchUI())
        self.errorLabel = Label(self.window, text="Username or password is incorrect", bg='white', fg="red", font=("Arial", 22, 'bold'))
        self.UI = [self.topText, self.userNameEntry,
                   self.passwordEntry, self.confirmButton,
                   self.errorLabel]
        self.opened = False

    def switchUI(self):
        if not self.opened:
            self.topText.place(x=640, y=150, anchor=CENTER)
            self.userNameEntry.place(x=640, y=300, anchor=CENTER)
            self.passwordEntry.place(x=640, y=400, anchor=CENTER)
            self.confirmButton.place(x=640, y=500, anchor=CENTER)
            self.errorLabel.place(x=640, y=600, anchor=CENTER)
            self.opened = True
        else:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False


