from tkinter import *
from tkmacosx import Button
import json

class LeaderboardUI:
    def __init__(self, window, buttonController, db):
        self.db = db
        self.window = window.window
        self.buttonController = buttonController

        self.topText = Label(self.window, text="Leaderboard",
                             font=("Arial", 70, 'bold'), fg="black", bg="white")
        self.opened = False
        self.backImage = PhotoImage(file='Images/backImage.png').subsample(x=13, y=13)
        self.backButton = Button(self.window, image=self.backImage, height=50, width=50,
                                 bg='white', fg='white', command=lambda: self.buttonController.changeClick('statisticUI'))
        self.player1 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player2 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player3= Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player4 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player5 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player6 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player7 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player8 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player9 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")
        self.player10 = Label(self.window, text='', width=1100, font=("Arial", 30, 'bold'), fg="black", bg="white")

        self.players = [self.player1, self.player2, self.player3, self.player4, self.player5, self.player6, self.player7, self.player8, self.player9, self.player10]

        self.UI = [
            self.topText,
            self.backButton,
            self.player1,
            self.player2,
            self.player3,
            self.player4,
            self.player5,
            self.player6,
            self.player7,
            self.player8,
            self.player9,
            self.player10,
        ]

    def switchUI(self):
        if not self.opened:
            inf = self.db.getBestPlayers()
            try:
                for i in range(10):
                    try:
                        self.players[i].config(text=f'{inf[i][0]} - level {inf[i][5]} ({inf[i][4]} xp): wins: {inf[i][1]}, losses: {inf[i][2]}')
                        self.players[i].place(x=640, y=200+i*50, anchor='center')
                    except:
                        pass
            except:
                pass
            self.topText.place(x=640, y=110, anchor='center')
            self.backButton.place(x=100, y=100, anchor='center')
            self.opened = True
        else:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except: pass
            self.opened = False