from ButtonControllerClass import ButtonController
from WindowClass import Window
from StartUIClass import StartUI
from LogInUIClass import LogInUI
from SingUpClass import SingUpUI
from TipTextClass import TipText
from MailUIClass import MailUI
from DB import dataBase

window = Window()
db = dataBase()
buttonController = ButtonController(window)
tipText = TipText()
startUI = StartUI(window, buttonController)
logInUI = LogInUI(window, db, buttonController, tipText)
singUpUI = SingUpUI(window, db, buttonController, tipText)
mainUI = MailUI(window, buttonController, db)

buttonController.addStates(startUI, logInUI, singUpUI, mainUI)
startUI.switchUI()
mainUI.autoOpen()

window.openWindow()