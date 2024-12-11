from tkinter import *
from tkmacosx import Button
import random
import json

class GameUI:
    """
    Класс игровой UI
    поля:
    текстовые поля для различных подписей
    кнопка подтверждения выбора и кнопка назад, кнопка перезапуска игры
    текстовые поля для вывода кто выиграл
    фото (3 штуки) для изображения всех кубиков
    весь UI хранится в специальном списке
    """
    def __init__(self, window, buttonController, db):
        self.window = window.window
        self.buttonController = buttonController
        self.db = db
        self.i = 0
        self.opened = False

        self.hm_bricks = random.randint(12, 20)
        self.backImage = PhotoImage(file='Images/backImage.png').subsample(x=13, y=13)
        self.backButton = Button(self.window, image=self.backImage, height=50, width=50,
                                 bg='white', fg='white', command=lambda: self.buttonController.changeClick('mainUI'))
        # текст, выводимый при ошибках ввода пользователя
        self.error_choice = Label(self.window, text="To Enter you need to choose an option!", bg="white", fg="red", font=("Arial", 10, "bold"))
        self.cant_choise_error = Label(self.window, text="You can not take more than in the heap", bg="white", fg="red", font=("Arial", 10, "bold"))
        
        # выпадающий список с вариантами выбора: сколько хочет взять пользователь кубиков
        self.var = IntVar()
        self.var.set(0)
        self.user_radiobutton_1 = Radiobutton(self.window, text='1', variable=self.var, value=1, foreground='black', font=("Arial", 20, 'bold'), bg='white')
        self.user_radiobutton_2 = Radiobutton(self.window, text='2', variable=self.var, value=2, foreground='black', font=("Arial", 20, 'bold'), bg='white')
        self.user_radiobutton_3 = Radiobutton(self.window, text='3', variable=self.var, value=3, foreground='black', font=("Arial", 20, 'bold'), bg='white')

        # кнопка сохранения выбора количества кубиков
        self.save_choise_button = Button(self.window, text='Enter', command=lambda: self.made_choise(self.var.get()), height=30, width=70,  fg="white", bg='black',font=("Arial", 20, "bold"))
        
        # текст для объяснения действий пользователю
        self.choice_lable = Label(self.window, text='Take some bricks from heap:', bg="white", fg="black", font=("Arial", 20, "bold"))

        self.playAgainButton =  Button(self.window, text='Play again', command=lambda: self.restartGame(), height=60, width=300,  fg="white", bg='black',font=("Arial", 40, "bold"))


        # текст хода пользователя
        self.user_move_text = Label(self.window, text='Your turn', bg="white", fg="black", font=("Arial", 30, 'bold'))
        
        # текст хода компьютера
        self.pc_move_text = Label(self.window, text='PC turn', bg="white", fg="black", font=("Arial", 30, 'bold'))
        
        # текст победы игрока
        self.win_label = Label(self.window, text='YOU WIN !!!', bg="white", fg="black", font=("Arial", 30, "bold"))
        
        # текст победы компьютера
        self.pc_win_label = Label(self.window, text='YOU LOST!!!', bg="white", fg="black", font=("Arial", 30, "bold"))
        
        # текст результата выбора компьютера
        self.pc_choice_label = Label(self.window, bg="white", fg="black", font=("Arial", 30, "bold"))
        
        # фото иконки пользователя
        self.user_icon_file = PhotoImage(file="Images/Game/images/user_icon.png").subsample(3,3)
        self.user_icon = Label(self.window, image=self.user_icon_file, height=200, width=200, bg="white")
        
        # фото иконки компьютера
        self.pc_ai_icon_file = PhotoImage(file="Images/Game/images/PCicon.png").subsample(3,3)
        self.pc_ai_icon = Label(self.window, image=self.pc_ai_icon_file, height=200, width=200, bg="white")

        self.name = None
        
        # подпись имени пользователя
        self.user_name = Label(self.window, text="User", bg="white", foreground="black", font=("Arial", 24, 'bold'))

        # подпись имени компьютера
        self.pc_name = Label(self.window, text='PC AI', bg="white", foreground="black", font=("Arial", 24, 'bold'))

        # текст с общим количеством кубиков в куче
        self.top_text = Label(self.window, text=f"The number of bricks is {self.hm_bricks}",foreground="black", font=("Arial", 42, 'bold'), bg="white")
        self.pc_wait_label = Label(self.window, text='.', bg="white", fg="black", font=("Arial", 30, "bold"))
        
        # фото всех кубиков
        self.all_bricks_file = PhotoImage(file="Images/Game/images/Bricks/AllBricks.png").subsample(3,3)
        self.all_bricks = Label(self.window, image=self.all_bricks_file, bg="white")

        # фото среднего количество кубиков
        self.middle_bricks_file = PhotoImage(file='Images/Game/images/Bricks/MiddleBricks.png').subsample(3,3)
        self.middle_bricks = Label(self.window, image=self.middle_bricks_file, bg="white")
        
        # фото малого количества кубиков
        self.little_bricks_file = PhotoImage(file='Images/Game/images/Bricks/LittleBricks.png').subsample(3,3)
        self.little_bricks = Label(self.window, image=self.little_bricks_file, bg="white")

        self.user_choise_text = None

        self.UI = [
            self.error_choice, self.cant_choise_error, self.user_radiobutton_1,
            self.user_radiobutton_2, self.user_radiobutton_3, self.save_choise_button,
            self.choice_lable, self.user_move_text, self.pc_move_text, self.win_label,
            self.pc_win_label, self.pc_choice_label, self.user_icon, self.pc_ai_icon,
            self.user_name, self.pc_name, self.top_text, self.pc_wait_label, self.all_bricks_file,
            self.middle_bricks, self.little_bricks, self.user_choise_text,
            self.playAgainButton, self.all_bricks, self.backButton
        ]

    # метод включения / выключения UI в зависимости от поля OPENED
    def switchUI(self):
        if not self.opened:
            with open('config.json', 'r') as file:
                data = json.load(file)
            self.name = data['userName']
            self.hm_bricks = random.randint(12, 20)
            self.top_text.config(text=f"The number of bricks is {self.hm_bricks}")
            self.user_name.config(text=self.name)

            self.i = 0
            self.var.set(0)
            self.backButton.place(x=100, y=100, anchor=CENTER)
            self.user_icon.place(x=170, y=200)
            self.pc_ai_icon.place(x=900, y=200)
            self.user_name.place(x=270, y=420, anchor=CENTER)
            self.pc_name.place(x=965, y=400)
            self.top_text.place(x=400, y=80)
            self.all_bricks.place(x=560, y=200)
            self.user_choice()
            self.opened = True
        else:
            for ui in self.UI:
                try:
                    ui.place_forget()
                except: pass
            self.opened = False

    # метод перезагрузки игры
    def restartGame(self):
        self.switchUI()
        self.switchUI()

        # метод изменения фотографии количества кубиков от его количества
    def new_photo(self):
        if self.hm_bricks < 5:
            try:
                self.middle_bricks.place_forget()
            except:
                pass
            try:
                self.little_bricks.place(x=500, y=200)
            except:
                pass
        elif self.hm_bricks < 10:
            try:
                self. all_bricks.place_forget()
            except:
                pass
            try:
                self.middle_bricks.place(x=560, y=200)
            except:
                pass

    # метод хода компьютера с последующей обработкой
    def plus_dot(self, label, i):
        try:
            self.user_move_text.place_forget()
        except:
            pass
        try:
            self.pc_move_text.place(x=950, y=150)
        except:
            pass
        self.new_photo()
        try:
            self.pc_choice_label.place_forget()
        except:
            pass
        if i == 0:
            self.pc_wait_label.place(x=965, y=450)
            self.pc_wait_label.config(text='.')
        elif i == 1:
            self.pc_wait_label.config(text='.  .')
        elif i == 2:
            self.pc_wait_label.config(text='.  .  .')
        if 0 <= i <= 2:
            self.window.after(200, self.plus_dot, label, i+1)
        else:
            i = 0
            self.pc_wait_label.place_forget()
            label.place_forget()
            pc_choice = random.randint(1, 3)
            if 1 <= self.hm_bricks <= 3:
                pc_choice = self.hm_bricks
            self.hm_bricks -= pc_choice
            self.top_text.config(text=f"The number of bricks is {self.hm_bricks}")
            self.pc_choice_label.config(text=f'PC choice {pc_choice}')
            self.pc_choice_label.place(x=920, y=450)
            if self.hm_bricks == 0:
                self.pc_win_label.place(x=190, y=450)
                with open('Config.json', mode='r') as file:
                    inf = json.load(file)
                    if self.db.logIn(inf['userName'], inf['password'], b=False) != []:
                        self.db.rewriteStatistics(inf['userName'], plusLoses=1, plusXP=5)
                        self.playAgainButton.place(x=640, y=650, anchor=CENTER)
                    # сохранение результатов игры в файл после победы компьютера
                return 0

            self.user_choice()
            return 0

    # метод, вызываемый после сохранения результата выбора пользователя с последующей обработкой
    def made_choise(self, choise):
        if choise == 0:
            try:
                self.cant_choise_error.place_forget()
            except:
                pass
            self.error_choice.place(x=300, y=570)
        elif choise > self.hm_bricks:
            try:
                self.error_choice.place_forget()
            except:
                pass
            self.cant_choise_error.place(x=300, y=570)
        else:
            try:
                self.error_choice.place_forget()
            except:
                pass
            try:
                self.cant_choise_error.place_forget()
            except:
                pass

            if choise == self.hm_bricks:
                self.hm_bricks -= choise
                self.win_label.place(x=190, y=450)
                self.user_move_text.place_forget()
                self.user_radiobutton_1.place_forget()
                self.user_radiobutton_2.place_forget()
                self.user_radiobutton_3.place_forget()
                self.save_choise_button.place_forget()
                self.choice_lable.place_forget()
                self.pc_choice_label.place_forget()
                self.top_text.config(text=f"The number of bricks is {self.hm_bricks}")
                with open('Config.json', mode='r') as file:
                    inf = json.load(file)
                    if self.db.logIn(inf['userName'], inf['password'], b=False) is not []:
                        self.db.rewriteStatistics(inf['userName'], plusWins=1, plusXP=25)
                        self.playAgainButton.place(x=640, y=650, anchor=CENTER)

            else:
                self.hm_bricks -= choise
                self.user_choise_text = Label(text=f'You choice {choise}', bg="white", fg="black", font=("Arial", 30, 'bold'))
                self.top_text.config(text=f'The number of bricks is {self.hm_bricks}')
                self.user_choise_text.place(x=190, y=450)
                self.user_radiobutton_1.place_forget()
                self.user_radiobutton_2.place_forget()
                self.user_radiobutton_3.place_forget()
                self.save_choise_button.place_forget()
                self.choice_lable.place_forget()
                self.plus_dot(self.user_choise_text, self.i)

    # метод, выводящий UI для выбора пользователя
    def user_choice(self):
        try:
            self.pc_move_text.place_forget()
        except:
            pass
        self.new_photo()
        self.user_move_text.place(x=200, y=150)
        self.user_radiobutton_1.place(x=210, y=490)
        self.user_radiobutton_2.place(x=210, y=530)
        self.user_radiobutton_3.place(x=210, y=570)
        self.save_choise_button.place(x=300, y=531)
        self.choice_lable.place(x=145, y=450)


