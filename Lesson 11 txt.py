#import os

"""f = open('students.txt', 'r')
max_line = ""
for row in f:
    if len(row) > len(max_line):
        max_line = row
print(max_line)
f.close()"""
"""import os

file = open('info.txt', 'r')
txt = file.read()
file.close()

var = ""
for word in txt.split():
    if word == "my":
        var += "your"
    else:
        var += " " + word + " "

file = open('info.txt', 'w')
file.write(var)"""

"""import os

file = open('numbers.txt', 'r')
string_numbers = file.read()
file.close()

arr = []
for num in string_numbers.split():
    arr.append(int(num))

result = str(max(arr)) + " " + str(min(arr))

try:
    file = open('info.txt', 'w')
    file.write(result)
    file.close()
except:
    print("error")"""

"""import os

file = open('numbers.txt', 'r')
string_numbers = file.read()
file.close()

arr = []
for row in string_numbers.split():
    arr.append(int(row))

arr.sort()
result = ""
for elem in arr:
    result += str(elem) + '\n'

try:
    file = open('info.txt', 'w')
    file.write(result)
    file.close()
except:
    print("error")"""

"""import os

file = open('info.txt', 'r')
text = file.read()

for row in text.split('\n'):
    print(str(len(row)) + " symbols")"""

import os

class User:
    id = int()
    login = str()
    password = str()

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password

    def toString(self):
        return str("\n" + str(self.id) + " " + self.login + " " + self.password)


class Main:
    def getuserList():
        file = open('info.txt', 'r')
        text = file.read()
        for row in text.split("\n"):
            print(row, end = "\n")
        file.close()

    def saveUser(text):
        file = open('info.txt', 'a')
        text_buffer = text
        file.write(text_buffer)
        file.close()


    while True:
        choice = int(input(""" 
    PRESS [1] TO ADD USERS
    PRESS [2] TO LIST USERS
    PRESS [3] TO EXIT\n"""))

        if 0 <= choice <= 3:
            if choice == 1:
               try:
                    id = int(input("Enter id: "))
                    login = input("Enter login: ")
                    password = input("Enter password: ")
                    user = User(id, login, password)
                    saveUser(user.toString())
                    continue
               except:
                   continue
            elif choice == 2:
                getuserList()
                continue
            else:
                print("Exiting")
                break


