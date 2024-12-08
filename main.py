from WindowClass import Window
from StartUIClass import StartUI
from LogInUIClass import LogIn

window = Window()
startUI = StartUI(window)
logInUI = LogIn(window)

logInUI.switchUI()
window.openWindow()