from s_taper import *
from s_taper.consts import *
from hashlib import md5

class dataBase:
    def __init__(self):
        self.usersInfScheme = {
            'UserName': TEXT,
            'Email': TEXT,
            'password': TEXT,
            'Level': INT,
            'XP': INT
        }
        self.db = Taper('UsersInf', 'Game/identifier.sqlite').create_table(self.usersInfScheme)

    def checkAccount(self, userName):
        inf = self.db.read('UserName', userName)
        if inf == []:
            inf = self.db.read('Email', userName)
        if inf == []:
            return False
        else:
            return True

    def logIn(self, userName, password):
        inf = self.db.read('UserName', userName)
        if inf == []:
            inf = self.db.read('Email', userName)
        if inf != []:
            if md5(password.encode()).hexdigest() == inf[2]:
                return inf
            else:
                return []
