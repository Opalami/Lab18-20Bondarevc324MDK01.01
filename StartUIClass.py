from tkinter import *
from tkmacosx import Button

class StartUI:
    def __init__(self, window, buttonController):
        self.windowClass = window
        self.window = window.window
        self.opened = False
        self.buttonController = buttonController

        self.topText = Label(self.window, text="Welcome to BriKet",
                        font=("Arial", 80), fg="black", bg="white")

        self.logInButton = Button(self.window, text='Log in', font=("Arial", 32, "bold"),
                             fg="white", bg='black', width=300, height=60,
                                  command=lambda: self.buttonController.changeClick('logInUI'))

        self.singUpButton = Button(self.window, text='Sing Up', font=("Arial", 32, 'bold'),
                                   fg="white", bg='black', width=300, height=60)

        self.exitButton = Button(self.window, text='Exit', font=("Arial", 32, 'bold'),
                                 fg="white", bg='black', width=300, height=60,
                                 command=lambda: self.windowClass.closeWindow())

        self.UI = [self.topText, self.logInButton,
                   self.singUpButton, self.exitButton]

    def switchUI(self):
        if self.opened:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False
        else:
            self.topText.place(x=640, y=150, anchor=CENTER)
            self.logInButton.place(x=640, y=300, anchor=CENTER)
            self.singUpButton.place(x=640, y=400, anchor=CENTER)
            self.exitButton.place(x=640, y=500, anchor=CENTER)
            self.opened = True

