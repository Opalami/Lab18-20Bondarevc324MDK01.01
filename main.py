from ButtonControllerClass import ButtonController
from WindowClass import Window
from StartUIClass import StartUI
from LogInUIClass import LogInUI
from SingUpClass import SingUpUI
from TipTextClass import TipText
from MailUIClass import MailUI
from GameUIClass import GameUI
from StatisticUIClass import StatisticUI
from LeaderboardUIClass import LeaderboardUI
from DB import dataBase

window = Window()
db = dataBase()
buttonController = ButtonController(window)
tipText = TipText()
startUI = StartUI(window, buttonController)
logInUI = LogInUI(window, db, buttonController, tipText)
singUpUI = SingUpUI(window, db, buttonController, tipText)
mainUI = MailUI(window, buttonController, db)
gameUI = GameUI(window, buttonController, db)
statisticUI = StatisticUI(window, db, buttonController)
leaderboardUI = LeaderboardUI(window, buttonController, db)

buttonController.addStates(startUI, logInUI, singUpUI, mainUI, gameUI, statisticUI, leaderboardUI)
startUI.switchUI()
mainUI.autoOpen()

window.openWindow()