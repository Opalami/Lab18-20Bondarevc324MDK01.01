

class ButtonController:
    def __init__(self, window):
        self.state = 'startUI'
        self.switches = {}
        self.startUI = None
        self.window = window
        self.logInUI = None

    def changeClick(self, newState):
        fun = self.switches[self.state]
        fun()
        self.state = newState
        fun = self.switches[self.state]
        fun()


    def addStates(self, startUI, logInUI, singUpUI, mainUI, gameUI):
        self.switches = {
            'startUI': startUI.switchUI,
            'logInUI': logInUI.switchUI,
            'singUpUI': singUpUI.switchUI,
            'mainUI': mainUI.switchUI,
            'gameUI': gameUI.switchUI
        }
