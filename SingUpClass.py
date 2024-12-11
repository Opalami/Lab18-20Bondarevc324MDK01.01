
from tkinter import *
from tkmacosx import Button
from LogInUIClass import LogInUI
import json

class SingUpUI(LogInUI):
    def __init__(self, window, db, buttonController, tipText):
        super().__init__(window, db, buttonController, tipText)
        self.seeAgainPassword = False
        self.genderChoice = StringVar()
        self.genderChoice.set('None')
        self.radiobuttonMale = Radiobutton(self.window, text= 'Male', variable=self.genderChoice,
                                           value='Male', font=("Arial", 20), bg='white', fg='black', selectcolor='blue')
        self.radiobuttonFemale = Radiobutton(self.window, text= 'Female', variable=self.genderChoice,
                                             value='Female', font=("Arial", 20), bg='white', fg='black', selectcolor='blue')
        self.genderText = Label(self.window, text="Gender", font=("Arial", 24, 'bold'), fg="black", bg="white")

        self.haveAccount = Label(self.window, text="Already have an account?", font=("Arial", 20, 'bold'), fg="black", bg="white")
        self.logInButton = Button(self.window, text='Log in ->', font=("Arial", 12, 'bold'),
                                fg="white", bg='black', width=70, height=30,
                                command=lambda: self.buttonController.changeClick('logInUI'))
        self.topText.config(text='Sing up')
        self.userEmailEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center')
        self.againPasswordEntry = Entry(self.window, width=24, fg="white",
                                   bg='black', font=("Arial", 32), justify='center')
        self.userNameEntry.config()
        self.userNameText.config(text='Username')
        self.showPassword.bind("<Button-1>", lambda _:self.switchShowPassword())
        self.emailText = Label(self.window, text="Email", font=("Arial", 16, 'bold'), fg="black", bg="white")
        self.againPasswordText = Label(self.window, text="Repeat password", font=("Arial", 16, 'bold'), fg="black", bg="white")
        self.againPasswordEntry.insert(0, "password")

        self.userEmailEntry.bind('<FocusIn>', lambda _: self.tipText.onFocus(self.userEmailEntry, 'example@mail.com'))
        self.userEmailEntry.bind('<FocusOut>', lambda _: self.tipText.offFocus(self.userEmailEntry, 'example@mail.com'))
        self.userEmailEntry.insert(0, 'example@mail.com')
        self.showAgainPassword = Label(self.window, image=self.closeEye, height=50, width=50,
                                  bg='white', fg='white')
        self.showAgainPassword.config(state=DISABLED)
        self.showAgainPassword.bind("<Button-1>", lambda _: self.switchShowAgainPassword())
        self.passwordEntry.bind('<FocusIn>', lambda _: self.tipText.onFocusForPassword
        (self.passwordEntry, self.showPassword, self.seePassword, self.switchShowPassword))
        self.passwordEntry.bind('<FocusOut>', lambda _: self.tipText.offFocusForPassword
        (self.passwordEntry, self.showPassword, self.seePassword, self.switchShowPassword))

        self.againPasswordEntry.bind('<FocusIn>', lambda _: self.tipText.onFocusForPassword
        (self.againPasswordEntry, self.showAgainPassword, self.seeAgainPassword, self.switchShowAgainPassword))
        self.againPasswordEntry.bind('<FocusOut>', lambda _: self.tipText.offFocusForPassword
        (self.againPasswordEntry, self.showAgainPassword, self.seeAgainPassword, self.switchShowAgainPassword))

        self.userNameError = Label(self.window, text="Password must be the same", bg='white', fg="red", font=("Arial", 16, 'bold'))
        self.emailError = Label(self.window, text="Password must be the same", bg='white', fg="red", font=("Arial", 16, 'bold'))
        self.passwordError = Label(self.window, text="Password must be the same", bg='white', fg="red", font=("Arial", 16, 'bold'))
        self.againPasswordError = Label(self.window, text="Password must be the same", bg='white', fg="red", font=("Arial", 16, 'bold'))
        self.genderChoiceError = Label(self.window, text="Gender must be choicen", bg='white', fg="red", font=("Arial", 16, 'bold'))

        self.clearButton = Button(self.window, text='Clear all', font=("Arial", 18, 'bold'),
                                 fg="white", bg='black', width=100, height=30,
                                 command=lambda: self.clearAllEntries())
        self.UI = [
            self.userEmailEntry, self.againPasswordEntry,
            self.topText, self.showPassword,
            self.userNameEntry, self.passwordEntry,
            self.confirmButton, self.backButton,
            self.passwordText, self.userNameText,
            self.againPasswordText, self.emailText,
            self.errorLabel, self.showAgainPassword,
            self.userNameError, self.emailError,
            self.passwordError, self.againPasswordError,
            self.radiobuttonMale, self.radiobuttonFemale,
            self.genderChoiceError, self.genderText, self.clearButton,
            self.logInButton, self.haveAccount
        ]
        self.errors = [self.userNameError, self.emailError,
                       self.passwordError, self.againPasswordError,
                       self.genderChoiceError]

        self.mainUI = [self.userNameEntry, self.userEmailEntry,
                       self.passwordEntry, self.againPasswordEntry]

        self.cordErrorsMainUI = [
            [375, 340],
            [375, 440],
            [905, 340],
            [905, 440]
        ]

        self.errorsText = [
            'Username must be written',
            'Email must be written',
            'Password must be written',
            'Repeat password must be written',
        ]

        self.mailUIDef = [
            'username', 'example@mail.com', 'password','password'
        ]

    def switchUI(self):
        if self.opened:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False
        else:
            if not self.seePassword:
                self.switchShowPassword()
            if not self.seeAgainPassword:
                self.switchShowAgainPassword()
            for ui in range(4):
                self.mainUI[ui].delete(0, 'end')
                self.mainUI[ui].insert(0, self.mailUIDef[ui])
            self.haveAccount.place(x=1100, y=70, anchor=CENTER)
            self.logInButton.place(x=1100, y=110, anchor=CENTER)
            self.showAgainPassword.config(state=DISABLED)
            self.genderChoice.set("None")
            self.genderText.place(x=640, y=470, anchor=CENTER)
            self.radiobuttonMale.place(x=570, y=500, anchor=CENTER)
            self.radiobuttonFemale.place(x=700, y=500, anchor=CENTER)
            self.showPassword.config(state=DISABLED)
            self.userNameEntry.config(fg='grey')
            self.passwordEntry.config(fg='grey')
            self.againPasswordEntry.config(fg='grey')
            self.userEmailEntry.config(fg='grey')
            self.topText.place(x=640, y=150, anchor=CENTER)
            self.showPassword.place(x=1200, y=300, anchor=CENTER)
            self.showAgainPassword.place(x=1200, y=400, anchor=CENTER)
            self.userNameEntry.place(x=375, y=300, anchor=CENTER)
            self.userEmailEntry.place(x=375, y=400, anchor=CENTER)
            self.passwordEntry.place(x=905, y=300, anchor=CENTER)
            self.againPasswordEntry.place(x=905, y=400, anchor=CENTER)
            self.confirmButton.place(x=640, y=600, anchor=CENTER)
            self.backButton.place(x=100, y=100, anchor=CENTER)
            self.passwordText.place(x=680, y=250)
            self.againPasswordText.place(x=680, y=350)
            self.userNameText.place(x=150, y=250)
            self.emailText.place(x=150, y=350)
            self.clearButton.place(x=400, y=600, anchor=CENTER)
            self.opened = True

    def clearAllEntries(self):
        for ui in range(4):
            self.mainUI[ui].delete(0, 'end')
            self.mainUI[ui].insert(0, self.mailUIDef[ui])
            self.mainUI[ui].config(fg='grey')
        self.showAgainPassword.config(state=DISABLED)
        self.genderChoice.set("None")
        self.showPassword.config(state=DISABLED)
        if not self.seePassword:
            self.switchShowPassword()
        if not self.seeAgainPassword:
            self.switchShowAgainPassword()

    def switchShowPassword(self):
        if not self.seePassword:
            self.showPassword.config(image=self.openEye)
            self.passwordEntry.config(show='')
            self.seePassword = True
        else:
            self.showPassword.config(image=self.closeEye)
            self.passwordEntry.config(show='*')
            self.seePassword = False


    def switchShowAgainPassword(self):
        if not self.seeAgainPassword:
            self.showAgainPassword.config(image=self.openEye)
            self.againPasswordEntry.config(show='')
            self.seeAgainPassword = True
        else:
            self.showAgainPassword.config(image=self.closeEye)
            self.againPasswordEntry.config(show='*')
            self.seeAgainPassword = False


    def checkPassword(self):
        if self.passwordEntry.get() == self.againPasswordEntry.get():
            return True
        else:
            self.againPasswordError.config(text='Passwords must be the same')
            self.againPasswordError.place(x=905, y=450, anchor=CENTER)
            return False

    def checkWritenEntries(self):
        error = False
        for i in range(4):
            if self.mainUI[i].get() == self.mailUIDef[i] or self.mainUI[i].get().strip() == '':
                self.errors[i].config(text=self.errorsText[i])
                self.errors[i].place(x=self.cordErrorsMainUI[i][0] ,y=self.cordErrorsMainUI[i][1], anchor=CENTER)
                error = True
        if self.genderChoice.get() == 'None':
            self.genderChoiceError.place(x=640, y=530, anchor=CENTER)
            error = True
        return not error

    def checkSecPassword(self):
        password = self.passwordEntry.get()
        if len(password) < 7:
            self.againPasswordError.config(text='Password must be at least 8 characters long')
            self.againPasswordError.place(x=905, y=440, anchor=CENTER)
            return False
        numbers = 0
        simbols = 0
        for char in password:
            if char.isdigit():
                numbers += 1
            else:
                simbols += 1
        if simbols < 3:
            self.againPasswordError.config(text='Password must contain at least 3 letters')
            self.againPasswordError.place(x=905, y=440, anchor=CENTER)
            return False
        if numbers < 3:
            self.againPasswordError.config(text='Password must contain at least 3 numbers')
            self.againPasswordError.place(x=905, y=440, anchor=CENTER)
            return False
        if not any(char in "@.,:;!_*-=()/#%&" for char in password):
            self.againPasswordError.config(text='Password must contain at least 1 special character')
            self.againPasswordError.place(x=905, y=440, anchor=CENTER)
            return False
        return True

    def checkNameEmail(self, username, email):
        error = False
        if not self.db.checkNewName(username):
            self.userNameError.config(text='Username already exists')
            self.userNameError.place(x=375, y=340, anchor=CENTER)
            error = True
        if not self.db.checkNewEmail(email):
            self.emailError.config(text='Email already exists')
            self.emailError.place(x=375, y=440, anchor=CENTER)
            error = True
        return not error

    def checkEmail(self, email):
        if not((len(email.split('@')) == 2 and '.' in email.split('@')[1]
               and len(email.split('@')[1].split('.')) == 2 and email.split('@')[1].split('.')[0].isalnum()
                    and email.split('@')[1].split('.')[1].isalnum()
               and any(char in 'qwertyuioplkjhgfdsazxcvbnm' for char in email.split('@')[1].split('.')[1])
        and any(char in 'qwertyuioplkjhgfdsazxcvbnm' for char in email.split('@')[1].split('.')[0])) and any(char in 'qwertyuioplkjhgfdsazxcvbnm' for char in email.split('@')[0])):
            self.emailError.config(text='Enter email correctly')
            self.emailError.place(x=375, y=440, anchor=CENTER)
            return False
        if any(char in ",:;!*=()/#%&" for char in email):
            self.emailError.config(text='Email cannot contain special characters')
            self.emailError.place(x=375, y=440, anchor=CENTER)
            return False
        return True

    def checkName(self, name):
        if not any(char in 'qwertyuioplkjhgfdsazxcvbnm' for char in name):
            self.userNameError.config(text='Name cannot contain with out letters')
            self.userNameError.place(x=self.cordErrorsMainUI[0][0], y=self.cordErrorsMainUI[0][1], anchor=CENTER)
            return False
        if len(name) > 20:
            self.userNameError.config(text='Name is too long')
            self.userNameError.place(x=self.cordErrorsMainUI[0][0], y=self.cordErrorsMainUI[0][1], anchor=CENTER)
            return False
        return True

    def checkData(self):
        username = self.userNameEntry.get()
        email = self.userEmailEntry.get()
        password = self.passwordEntry.get()
        gender = self.genderChoice.get()
        for error in self.errors:
            try:
                error.place_forget()
            except:
                pass
        if self.checkWritenEntries():
            if self.checkEmail(email):
                if self.checkName(username):
                    if self.checkNameEmail(username, email):
                        if self.checkPassword():
                            if self.checkSecPassword():
                                self.db.singUp(username, email, password, gender)
                                self.buttonController.changeClick('mainUI')














