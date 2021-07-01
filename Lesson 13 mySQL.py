import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bitlab"
)

mycursor = mydb.cursor()

def addUser(login, name, surname, age)
  global mydb
  mycursor = mydb.cursor()
  sql = "INSERT INTO users (id, login, name, surname, age) VALUES (NULL, %s, %s, %s, %s)"
  values = (login, name, surname, age)
  mycursor.execute(sql, values)
  mydb.commit()


def getUsers():
  global mydb
  mycursor = mydb.cursor()
  sql = "SELECT * FROM users ORDER BY age DESC"
  mycursor.execute(sql)
  result = mycursor.fetchall()
  return result


def deleteUser(id):
  global mydb
  mycursor = mydb.cursor()
  sql = "DELETE FROM users WHERE id = " + str(id)
  mycursor.execute(sql)
  mydb.commit()


def updateUser(id, login, name, surname, age):
  global mydb
  mycursor = mydb.cursor()
  sql = "UPDATE users SET login = %s, name = %s, surname = %s, age = %s WHERE id = " + str(id)
  values = (login, name, surname, age)
  mycursor.execute(sql, values)
  mydb.commit()


while True:
  print("PRESS 1 TO ADD USER")
  print("PRESS 2 TO LIST USERS")
  print("PRESS 3 TO DELETE USER")
  print("PRESS 4 TO UPDATE USER")
  print("PRESS 0 TO EXIT")

  choice = input()

  if choice == "1":
    print("INSERT LOGIN:")
    login = input()
    print("INSERT NAME:")
    name = input()
    print("INSERT SURNAME:")
    surname = input()
    print("INSERT AGE:")
    age = input()

    addUser(login, name, surname, age)

  elif choice == "2":
    users = getUsers()
    for user in users:
      print(user)

  elif choice == "3":
    users = getUsers()
    for user in users:
      print(user)

    print("CHOOSE ID OF USER TO DELETE:")
    id = input()
    deleteUser(id)

  elif choice == "4":
    users = getUsers()
    for user in users:
      print(user)

    print("CHOOSE ID OF USER TO UPDATE:")
    id = input()

    print("INSERT NEW LOGIN:")
    login = input()
    print("INSERT NEW NAME:")
    name = input()
    print("INSERT NEW SURNAME:")
    surname = input()
    print("INSERT NEW AGE:")
    age = input()
    updateUser(id, login, name, surname, age)

  elif choice == "0":
    break

