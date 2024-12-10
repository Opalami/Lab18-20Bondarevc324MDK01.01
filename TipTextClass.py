from tkinter import *
from tkmacosx import Button

class TipText:

    def onFocus(self, entry, text):
        entry.config(fg='white')
        entryText = entry.get()
        if entryText == text:
            entry.delete(0, END)

    def offFocus(self, entry, text):
        entryText = entry.get()
        if entryText.strip() == '':
            entry.delete(0, END)
            entry.insert(0, text)
            entry.config(fg='grey')
        else:
            entry.delete(0, END)
            entryText = entryText.strip().split(' ')
            while True:
                if '' in entryText:
                    entryText.remove('')
                else:
                    break
            entry.insert(0, ''.join(entryText))

    def onFocusForPassword(self, entry, seeButton, canShow, switchShowPassword):
        entryText = entry.get()
        entry.config(fg='white')
        if entryText.strip() == 'password':
            if canShow:
                switchShowPassword()

            seeButton.config(state=ACTIVE)
            entry.delete(0, END)

    def offFocusForPassword(self, entry, seeButton, canShow, switchShowPassword):
        entryText = entry.get()
        if entryText.strip() == '':
            if not canShow:
                switchShowPassword()
            entry.config(fg='grey')
            seeButton.config(state=DISABLED)
            entry.delete(0, END)
            entry.insert(0, 'password')
        else:
            entry.delete(0, END)
            entryText = entryText.strip().split(' ')
            while True:
                if '' in entryText:
                    entryText.remove('')
                else:
                    break
            entry.insert(0, ''.join(entryText))




