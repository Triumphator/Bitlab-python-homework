"""import json
import  os

employee = [
    {"id": 1, "name": "Emily", "age": 35, "salary": 500000},
    {"id": 1, "name": "Jack", "age": 46, "salary": 450000},
    {"id": 1, "name": "Tom", "age": 29, "salary": 350000},
    {"id": 1, "name": "Fin", "age": 31, "salary": 400000},
    {"id": 1, "name": "Amanda", "age": 24, "salary": 250000},
    {"id": 1, "name": "Kate", "age": 30, "salary": 340000}
]

file = open('emloyee.json', 'w')
json.dump(employee, file)
file.close()

file = open('emloyee.json', 'r')
result = json.load(file)
file.close()
for elem in result:
    if elem['salary'] > 350000:
        print(elem["name"], " age ", elem["age"], " salary ", elem["salary"])"""

"""import json
import  os

users = {
    "user1": {"id": 1, "name": "Emily", "login": "emily@gmail.com", "password": "qwerty"},
    "user2": {"id": 2, "name": "Jack", "login": "jack@gmail.com", "password": "qwerty2"},
    "user3": {"id": 3, "name": "Tom", "login": "tom@gmail.com", "password": "qwerty3"}
}

file = open('user.json', 'w')
json.dump(users, file)
file.close()

file = open('user.json', 'r')
users_data = json.load(file)
file.close()

login = input("Enter login: ")
password = input("Enter password: ")
for person in users_data.values():
    if login == person["login"] and password == person["password"]:
        print("Hello, " + person["name"])
        break
else:
    print("Try again")"""

"""import json
import os

cart = {
 "orderID": 12345,
 "shopperName": "Ilyas Zhuanyshov",
 "shopperEmail": "ilyas@gmail.com",
 "products": [
   {
     "productID": 34,
     "productName": "apple",
     "price": 100,
     "quantity": 2
   },
   {
     "productID": 56,
     "productName": "banana",
     "price": 300,
     "quantity": 3
   },
  {
   "productID": 56,
   "productName": "ice-cream",
   "price": 1000,
   "quantity": 2
  },
  {
   "productID": 56,
   "productName": "cake",
   "price": 4000,
   "quantity": 1
  }
 ]
}

file = open('products.json', 'w')
json.dump(cart, file)
file.close()

file = open('products.json', 'r')
receipt = json.load(file)
file.close()

sum_cart = 0
for product in receipt["products"]:
    sum_cart += product['price'] * product['quantity']
print(sum_cart)"""

import os
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

    def getUserList():
        file = open('user.json', 'r')
        text = json.load(file)
        file.close()
        for key, value in text.items():
            print(key, ':', value)

    def saveUser(user):
        file = open('user.json', 'r')
        dict = json.load(file)
        file.close()
        file2 = open('user.json', 'w')
        dictUser = {"id" : user.id, "login" : user.login, "password" : user.password}
        dict["user" + str(user.id)] = dictUser

        json.dump(dict, file2)
        file2.close()


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
                    saveUser(user)
                    continue
               except:
                    print("Something went wrong")
                    continue
            elif choice == 2:
                getUserList()
                continue
            else:
                print("Exiting")
                break