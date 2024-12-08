from ButtonControllerClass import ButtonController
from WindowClass import Window
from StartUIClass import StartUI
from LogInUIClass import LogIn
from DB import dataBase

window = Window()
db = dataBase()
buttonController = ButtonController(window)
startUI = StartUI(window, buttonController)
logInUI = LogIn(window, db, buttonController)

buttonController.addStates(startUI, logInUI)
startUI.switchUI()

window.openWindow()