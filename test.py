import json


class User:
    id = int()
    login = str()
    password = str()

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password


class Main:
    def getUsersList():
        file = open('users.json', 'r')
        dict = json.load(file)
        print(dict, end=' ')

    def saveUser(user):
        file = open('users.json', 'w')
        dict = {
            'id': user.id,
            'login': user.login,
            'password': user.password
        }
        json.dump(dict, file)

    while True:
        choose = int(input(''' PRESS [1] TO ADD USERS 
     PRESS [2] TO LIST USERS 
     PRESS [4] TO EXIT\n'''))

        if choose == 1:
            id = int(input())
            login = input()
            password = input()
            user = User(id, login, password)
            saveUser(user)
        elif choose == 2:
            getUsersList()
        elif choose == 4:
            break


