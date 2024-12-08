class ButtonController:
    def __init__(self, window):
        self.state = 'startWindow'
        self.states = {'startWindow'}

    def changeClick(self, newState):
        self.state = newState
        


