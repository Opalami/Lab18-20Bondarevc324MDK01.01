from tkinter import *

class Window:
    """
    Класс игровое окно
    Поля:
    инициализированное окно tk с последующей настройкой
    текст, на котором указаны данные поддержки
    """
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.resizable(False, False)
        self.window.configure(bg="white")
        self.window.title('BriKet')
        self.helpLabel = Label(self.window, text="BriKet Help: Telegram @Maxim_B0nd", fg="black", bg="white", font=('Arial', 12, 'bold'))

    # метод открытия окна и помещения текста поддержки
    def openWindow(self):
        self.helpLabel.place(x=5, y=700)
        self.window.mainloop()

    # метод закрытия окна
    def closeWindow(self):
        self.window.destroy()



