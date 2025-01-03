from s_taper import *
from s_taper.consts import *
from hashlib import md5
import json

class dataBase:
    """
    класс база данных
    поля:
    шаблоны для инициализации таблиц SQLite
    инициализированные таблицы
    """
    def __init__(self):
        self.usersInfScheme = {
            'UserName': TEXT,
            'Email': TEXT,
            'password': TEXT,
            'Level': INT,
            'XP': INT,
            'Gender':TEXT
        }
        self.db = Taper('UsersInf', 'Game/identifier.sqlite').create_table(self.usersInfScheme)
        self.statisticsScheme = {
            'UserName': TEXT,
            'wins': INT,
            'loses': INT,
            'gamePlayed': INT,
            'xp': INT,
            'level': INT,
        }
        self.statistics = Taper('statistics', 'Game/identifier.sqlite').create_table(self.statisticsScheme)

    # метод проверки на существование аккаунта с данным именем/почтой
    def checkAccount(self, userName):
        inf = self.db.read('UserName', userName)
        if inf == []:
            inf = self.db.read('Email', userName)
        if inf == []:
            return False
        else:
            return True

    # метод входа в аккаунт с проверкой на корректность ввода данных
    def logIn(self, userName, password, b=True):
        inf = self.db.read('UserName', userName)

        if inf == []:
            inf = self.db.read('Email', userName)

        if inf != []:
            if b:
                if md5(password.encode()).hexdigest() == inf[2]:
                    return inf
                else:
                    return []
            else:
                if password == inf[2]:
                    return inf
                else:
                    return []
        return []

    # метод проверки на уникальность переданного имени
    def checkNewName(self, username):
        inf = self.db.read('UserName', username)
        if inf == []:
            return True
        else:
            return False

    # метод проверки на уникальность данной почты
    def checkNewEmail(self, email):
        inf = self.db.read('Email', email)
        if inf == []:
            return True
        else:
            return False

    # метод регистрации данных в БД и в файл config
    def singUp(self, userName, email, password, gender):
        self.db.write((userName, email, md5(password.encode()).hexdigest(), 1, 0, gender))
        self.statistics.write((userName, 0, 0, 0, 0, 1))
        newData = {
            "userName": userName,
            "userEmail": email,
            "password": md5(password.encode()).hexdigest(),
            "XP": 0,
            "level": 1,
            "Gender": gender
        }

        with open('config.json', 'w') as file:
            json.dump(newData, file)

    # метод очищения файла config
    def clearConfig(self):
        newData = {
            "userName": None,
            "userEmail": None,
            "password": None,
            "XP": 0,
            "level": 0,
            "Gender": None
        }

        with open('Config.json', 'w') as config:
            json.dump(newData, config)

    # метод получения статистики переданного пользователя
    def getStatistics(self, userName):
        inf = self.statistics.read('UserName', userName)
        if inf != []:
            return inf
        else:
            return []
    # метод перезаписи статистики
    def rewriteStatistics(self, userName, plusWins=0, plusLoses=0, plusXP=0):
        inf = self.statistics.read('UserName', userName)
        self.statistics.delete_row('UserName', userName)
        if (inf[4]+plusXP) // 400 >= inf[5]:
            plusLevel = 1
        else:
            plusLevel = 0
        newInf = (
            userName,
            inf[1]+plusWins,
            inf[2]+plusLoses,
            inf[3]+1,
            inf[4]+plusXP,
            inf[5]+plusLevel
        )
        self.statistics.write(newInf)

    # метод получения отсортированного списка с лучшими игроками
    def getBestPlayers(self):
        inf = self.statistics.read_all()
        inf.sort(key=lambda x: x[4], reverse=True)
        return inf


