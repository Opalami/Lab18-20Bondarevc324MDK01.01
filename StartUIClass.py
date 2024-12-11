from tkinter import *
from tkmacosx import Button

class StartUI:
    """
    Класс стартовый UI
    поля:
    инициализация окна, контроллер кнопок
    кнопки: зарегистрироваться, войти, выход
    текстовые поля: главная подпись посередине наверху
    весь UI хранится в специальном поле-списке
    """
    def __init__(self, window, buttonController):
        self.windowClass = window
        self.window = window.window
        self.opened = False
        self.buttonController = buttonController
        self.exitText = Label(self.window, text='Do you actually want to ', width=1100, font=("Arial", 50, 'bold'), fg="black", bg="white")
        self.yesButton = Button(self.window, text='Yes', font=("Arial", 32, 'bold'),
                                fg="white", bg='black', width=300, height=60,
                                command=lambda: self.windowClass.closeWindow())
        self.noButton = Button(self.window, text='No', font=("Arial", 32, 'bold'),
                               fg="white", bg='black', width=300, height=60,
                               command=lambda: self.windowClass.closeWindow())
        self.topText = Label(self.window, text="Welcome to BriKet",
                        font=("Arial", 100, 'bold'), fg="black", bg="white")
        self.logInButton = Button(self.window, text='Log in', font=("Arial", 32, "bold"),
                             fg="white", bg='black', width=300, height=60,
                                  command=lambda: self.buttonController.changeClick('logInUI'))
        self.singUpButton = Button(self.window, text='Sing Up', font=("Arial", 32, 'bold'),
                                   fg="white", bg='black', width=300, height=60,
                                   command=lambda: self.buttonController.changeClick('singUpUI'))
        self.exitButton = Button(self.window, text='Exit', font=("Arial", 32, 'bold'),
                                 fg="white", bg='black', width=300, height=60,
                                 command=lambda: self.existEnter('exit ?', self.windowClass.closeWindow,
                                                                 self.doubleSwitch))
        self.UI = [self.topText, self.logInButton,
                   self.singUpButton, self.exitButton,
                   self.yesButton, self.noButton, self.exitText]

    # метод включения / выключения UI в зависимости от поля OPENED
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

    # метод подтверждения действия (выводит диалоговое окно и спрашивает, хотим ли мы сделать "текст"
    # текст - переданный параметр
    # после выбора выполняет funcYes при нажатии на да
    # или funcNo при нажатии на нет
    def existEnter(self, text, funcYes, funcNo):
        self.exitText.config(text=f'Do you actually want to {text}')
        self.switchUI()
        self.noButton.config(command=lambda : funcNo())
        self.yesButton.config(command=lambda : funcYes())
        self.exitText.place(x=640, y=300, anchor=CENTER)
        self.noButton.place(x=440, y=450, anchor=CENTER)
        self.yesButton.place(x=840, y=450, anchor=CENTER)

    # метод перезагрузки UI (выключение и включение)
    def doubleSwitch(self):
        self.opened = True
        self.switchUI()
        self.switchUI()