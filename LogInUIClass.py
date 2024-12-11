from tkinter import *
from tkmacosx import Button
import json

class LogInUI:
    def __init__(self, window, db, buttonController, tipText):
        self.window = window.window
        self.db = db
        self.buttonController = buttonController
        self.tipText = tipText
        self.opened = False
        self.seePassword = False
        self.openEye = PhotoImage(file='Images/logInImages/OpenEye.png').subsample(x=13, y=13)
        self.closeEye = PhotoImage(file='Images/logInImages/CloseEye.png').subsample(x=13, y=13)
        self.backImage = PhotoImage(file='Images/backImage.png').subsample(x=13, y=13)

        self.topText = Label(self.window, text="Authorization",
                             font=("Arial", 80), fg="black", bg="white")
        self.userNameEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center')
        self.userNameEntry.insert(0, "username")
        self.userNameEntry.bind('<FocusOut>', lambda _: self.tipText.offFocus(self.userNameEntry, 'username'))
        self.userNameEntry.bind('<FocusIn>', lambda _: self.tipText.onFocus(self.userNameEntry, 'username'))

        self.passwordEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center', show='*')

        self.passwordEntry.bind('<FocusIn>', lambda _: self.tipText.onFocusForPassword(self.passwordEntry, self.showPassword, self.seePassword, self.switchShowPassword))
        self.passwordEntry.bind('<FocusOut>', lambda _: self.tipText.offFocusForPassword(self.passwordEntry, self.showPassword, self.seePassword, self.switchShowPassword))
        self.passwordEntry.insert(0, "password")

        self.dontHaveAccount = Label(self.window, text="Dot`n have an account?", font=("Arial", 20, 'bold'), fg="black",
                                 bg="white")
        self.singUpButton = Button(self.window, text='Sing up ->', font=("Arial", 12, 'bold'),
                                  fg="white", bg='black', width=70, height=30,
                                  command=lambda: self.buttonController.changeClick('singUpUI'))

        self.showPassword = Label(self.window, image=self.closeEye, height=50, width=50,
                                   bg='white', fg='white')
        self.showPassword.config(state=DISABLED)
        self.showPassword.bind("<Button-1>", lambda _:self.switchShowPassword())
        self.backButton = Button(self.window, image=self.backImage,  height=50, width=50,
                                   bg='white', fg='white', command=lambda : self.buttonController.changeClick('startUI'))
        self.userNameText = Label(self.window, text="Username/email", font=("Arial", 16, 'bold'), fg="black", bg="white")
        self.passwordText = Label(self.window, text="Password", font=("Arial", 16, 'bold'), fg="black", bg="white")

        self.confirmButton = Button(self.window, text="Confirm", height=60, width=300, fg="white", bg='black', font=("Arial", 32, 'bold'),
                                    command=lambda: self.checkData())
        self.errorLabel = Label(self.window, text="Username or password is incorrect", bg='white', fg="red", font=("Arial", 22, 'bold'))
        self.UI = [self.topText, self.userNameEntry,
                   self.passwordEntry, self.showPassword,
                   self.confirmButton, self.errorLabel,
                   self.backImage, self.backButton,
                   self.passwordText, self.userNameText,
                   self.dontHaveAccount, self.singUpButton]


    def switchUI(self):
        if not self.opened:
            if not self.seePassword:
                self.switchShowPassword()
            self.dontHaveAccount.place(x=1100, y=70, anchor=CENTER)
            self.singUpButton.place(x=1100, y=110, anchor=CENTER)
            self.showPassword.config(state=DISABLED)
            self.userNameEntry.config(fg='grey')
            self.passwordEntry.config(fg='grey')
            self.topText.place(x=640, y=150, anchor=CENTER)
            self.showPassword.place(x=900, y=400, anchor=CENTER)
            self.userNameEntry.place(x=640, y=300, anchor=CENTER)
            self.passwordEntry.place(x=640, y=400, anchor=CENTER)
            self.confirmButton.place(x=640, y=500, anchor=CENTER)
            self.backButton.place(x=100, y=100, anchor=CENTER)
            self.passwordText.place(x=415, y=350)
            self.userNameText.place(x=415, y=250)
            self.opened = True
        else:
            if self.seePassword:
                self.switchShowPassword()
            self.userNameEntry.delete(0, END)
            self.userNameEntry.insert(0, 'username')
            self.passwordEntry.delete(0, END)
            self.passwordEntry.insert(0, 'password')
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
        try:
            self.errorLabel.place_forget()
        except:
            pass
        userName = self.userNameEntry.get()
        password = self.passwordEntry.get()
        userData = self.db.logIn(userName, password)
        if userData != []:
            newData = {
                "userName": userData[0],
                "userEmail": userData[1],
                "password": userData[2],
                "XP": userData[4],
                "level": userData[3],
                "Gender": userData[5]
            }
            with open('Config.json', 'w') as config:
                json.dump(newData, config)
            self.buttonController.changeClick('mainUI')

        else:
            self.errorLabel.place(x=640, y=450, anchor=CENTER)

