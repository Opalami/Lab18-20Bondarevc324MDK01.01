from tkinter import *
from tkmacosx import Button
import json

class LogIn:
    def __init__(self, window, db, buttonController):
        self.window = window.window
        self.db = db
        self.buttonController = buttonController
        self.opened = False
        self.seePassword = False
        self.openEye = PhotoImage(file='Images/logInImages/OpenEye.png').subsample(x=13, y=13)
        self.closeEye = PhotoImage(file='Images/logInImages/CloseEye.png').subsample(x=13, y=13)
        self.backImage = PhotoImage(file='Images/backImage.png').subsample(x=13, y=13)

        self.topText = Label(self.window, text="Authorization",
                             font=("Arial", 80), fg="black", bg="white")
        self.userNameEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center')
        self.passwordEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center', show='*')

        self.showPassword = Label(self.window, image=self.closeEye, height=50, width=50,
                                   bg='white', fg='white')
        self.showPassword.bind("<Button-1>", lambda _:self.switchShowPassword())
        self.backButton = Label(self.window, image=self.backImage,  height=50, width=50,
                                   bg='white', fg='white')
        self.backButton.bind('<Button-1>', lambda _: self.buttonController.changeClick('startUI'))

        self.confirmButton = Button(self.window, text="Confirm", height=60, width=300, fg="white", bg='black', font=("Arial", 32, 'bold'),
                                    command=lambda: self.checkData())
        self.errorLabel = Label(self.window, text="Username or password is incorrect", bg='white', fg="red", font=("Arial", 22, 'bold'))
        self.UI = [self.topText, self.userNameEntry,
                   self.passwordEntry, self.showPassword,
                   self.confirmButton, self.errorLabel,
                   self.backImage, self.backButton]


    def switchUI(self):
        if not self.opened:
            self.topText.place(x=640, y=150, anchor=CENTER)
            self.showPassword.place(x=900, y=400, anchor=CENTER)
            self.userNameEntry.place(x=640, y=300, anchor=CENTER)
            self.passwordEntry.place(x=640, y=400, anchor=CENTER)
            self.confirmButton.place(x=640, y=500, anchor=CENTER)
            self.errorLabel.place(x=640, y=600, anchor=CENTER)
            self.backButton.place(x=100, y=100, anchor=CENTER)
            self.opened = True
        else:
            if self.seePassword:
                self.switchShowPassword()
            self.userNameEntry.delete(0, END)
            self.passwordEntry.delete(0, END)
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False


    def switchShowPassword(self):
        if not self.seePassword:
            self.showPassword.config(image=self.openEye)
            self.passwordEntry.config(show='')
            self.seePassword = True
        else:
            self.showPassword.config(image=self.closeEye)
            self.passwordEntry.config(show='*')
            self.seePassword = False

    def checkData(self):
        userName = self.userNameEntry.get()
        password = self.passwordEntry.get()
        userData = self.db.logIn(userName, password)
        if userData != []:
            newData = {
                "userName": userData[0],
                "userEmail": userData[1],
                "password": userData[2],
                "XP": userData[3],
                "level": userData[4]
            }
            with open('Config.json', 'w') as config:
                json.dump(newData, config)

        else:
            print('bad')
