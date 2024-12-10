from tkinter import *
from tkmacosx import Button
from StartUIClass import StartUI
import json

class MailUI(StartUI):
    def __init__(self, window, buttonController, db):
        super().__init__(window, buttonController)
        self.db = db
        self.topText.config(text='BriKet')
        self.logInButton.config(text='Game')
        self.singUpButton.config(text='Statistics')
        self.logInButton.config(command=lambda: self.buttonController.changeClick('gameUI'))
        self.singUpButton.config(command=lambda: self.buttonController.changeClick('statisticUI'))
        self.exitButton = Button(self.window, text='Exit', font=("Arial", 32, 'bold'),
                                 fg="white", bg='black', width=300, height=60,
                                 command=lambda: self.windowClass.closeWindow())
        self.nickname = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white", justify=RIGHT)
        self.level = Label(self.window, text='',  width=1100, font=("Arial", 18, 'bold'), fg="black", bg="white", justify=RIGHT)

        self.logUOutButton = Button(self.window, text='Log out', font=("Arial", 12, 'bold'),
                                 fg="white", bg='black', width=70, height=20,
                                 command=lambda: self.logOut())

        self.UI = [
            self.topText,
            self.logInButton,
            self.singUpButton,
            self.exitButton,
            self.nickname,
            self.level,
            self.logUOutButton
        ]

    def logOut(self):
        self.db.clearConfig()
        self.buttonController.changeClick('startUI')

    def switchUI(self):
        if self.opened:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False
        else:
            with open('config.json', 'r') as file:
                data = json.load(file)
            if self.db.logIn(data['userName'], data['password'], b=False) != []:
                inf = self.db.getStatistics(data['userName'])
                self.nickname.config(text=inf[0])
                self.level.config(text=f'Level {inf[5]} ({inf[4]} xp)')
                self.logUOutButton.place(x=640, y=620, anchor=CENTER)
                self.level.place(x=640, y=690, anchor=CENTER)
                self.nickname.place(x=640, y=650, anchor=CENTER)
                self.topText.place(x=640, y=150, anchor=CENTER)
                self.logInButton.place(x=640, y=300, anchor=CENTER)
                self.singUpButton.place(x=640, y=400, anchor=CENTER)
                self.exitButton.place(x=640, y=500, anchor=CENTER)
                self.opened = True
            else:
                self.db.clearConfig()
                self.buttonController.changeClick('startUI')

    def autoOpen(self):
        error = False
        with open('config.json', 'r') as file:

            data = json.load(file)
            inf = self.db.logIn(data['userName'], data['password'], b=False)
            print(inf)
            if inf != []:
                if data['userName'] == inf[0] and data['password'] == inf[2]:
                    self.buttonController.changeClick('mainUI')
                else:
                    error = True
            else:
                error = True
        if error:
            self.db.clearConfig()
            self.buttonController.changeClick('startUI')





