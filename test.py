import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bitlab"
)

mycursor = mydb.cursor()

sql = "INSERT INTO players (id, name, number, price) VALUES (NULL, %s, %s, %s)"
val = ("freddy", 9, 52000000)

mycursor.execute(sql, val)
mydb.commit()

sql = "SELECT * FROM players"
mycursor.execute(sql)

result = mycursor.fetchall()
for player in result:
  print(player)

print(mycursor.rowcount, " record inserted.")