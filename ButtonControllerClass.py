class ButtonController:
    """
    Класс контроллер кнопок
    поля:
    текущее состояние
    переключатели
    """
    def __init__(self, window):
        self.state = 'startUI'
        self.switches = {}
        self.window = window

    # метод выключения прошлого UI и включения нового
    def changeClick(self, newState):
        fun = self.switches[self.state]
        fun()
        self.state = newState
        fun = self.switches[self.state]
        fun()

    # метод добавления переключателей
    def addStates(self, startUI, logInUI, singUpUI, mainUI, gameUI, statisticUI, leaderboardUI):
        self.switches = {
            'startUI': startUI.switchUI,
            'logInUI': logInUI.switchUI,
            'singUpUI': singUpUI.switchUI,
            'mainUI': mainUI.switchUI,
            'gameUI': gameUI.switchUI,
            'statisticUI': statisticUI.switchUI,
            'leaderboardUI': leaderboardUI.switchUI
        }
