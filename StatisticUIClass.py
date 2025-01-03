from tkinter import *
from tkmacosx import Button
import json

class StatisticUI:
    """
    Класс статистика UI
    поля:
    инициализация окна, бд, контроллер кнопок
    объявление полей для выйгрыша, поражения, всего сыграно матчей, опыт, уровень
    кнопки: для перехода на прошлое окно, переход на доску лидеров
    весь UI хранится в специальном поле-списке
    """
    def __init__(self, window, db, buttonController):
        self.window = window.window
        self.db = db
        self.buttonController = buttonController
        self.opened = False
        self.topText = Label(self.window, text="Your statistics",
                             font=("Arial", 80, 'bold'), fg="black", bg="white")
        self.winsLabel = Label(self.window, text="",
                             font=("Arial", 50, 'bold'), fg="black", bg="white")
        self.losesLabel = Label(self.window, text="",
                             font=("Arial", 50, 'bold'), fg="black", bg="white")
        self.gamePlayedLabel = Label(self.window, text="",
                             font=("Arial", 50, 'bold'), fg="black", bg="white")
        self.xpLabel =Label(self.window, text="",
                             font=("Arial", 50, 'bold'), fg="black", bg="white")

        self.levelLabel =Label(self.window, text="",
                             font=("Arial", 50, 'bold'), fg="black", bg="white")

        self.backImage = PhotoImage(file='Images/backImage.png').subsample(x=13, y=13)
        self.backButton = Button(self.window, image=self.backImage, height=50, width=50,
                                 bg='white', fg='white', command=lambda: self.buttonController.changeClick('mainUI'))

        self.leaderBoardButton = Button(self.window, text='Leaderboard', font=("Arial", 32, 'bold'),
                                   fg="white", bg='black', width=300, height=60,
                                   command=lambda: self.buttonController.changeClick('leaderboardUI'))

        self.UI = [
            self.topText, self.winsLabel, self.losesLabel, self.gamePlayedLabel,
            self.xpLabel, self.levelLabel, self.backButton, self.leaderBoardButton
        ]
    # метод включения / выключения UI в зависимости от поля OPENED
    def switchUI(self):
        if not self.opened:
            with open('config.json', 'r') as file:
                data = json.load(file)
                if self.db.logIn(data['userName'], data['password'], b=False) != []:
                    inf = self.db.getStatistics(data['userName'])
                    self.leaderBoardButton.place(x=640, y=600, anchor=CENTER)
                    self.winsLabel.config(text=f'Wins: {inf[1]}')
                    self.losesLabel.config(text=f'Losses: {inf[2]}')
                    self.gamePlayedLabel.config(text=f'Game played: {inf[3]}')
                    self.xpLabel.config(text=f'XP: {inf[4]}')
                    self.levelLabel.config(text=f'Level: {inf[5]}')
                    self.topText.place(x=640, y=150, anchor=CENTER)
                    self.winsLabel.place(x=450, y=300, anchor=CENTER)
                    self.losesLabel.place(x=450, y=400, anchor=CENTER)
                    self.xpLabel.place(x=830, y=300, anchor=CENTER)
                    self.levelLabel.place(x=830, y=400, anchor=CENTER)
                    self.gamePlayedLabel.place(x=640, y=500, anchor=CENTER)
                    self.backButton.place(x=100, y=100, anchor=CENTER)
                    self.opened = True
                else:
                    self.db.clearConfig()
                    self.buttonController.changeClick('startUI')
        else:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except:
                    pass
            self.opened = False