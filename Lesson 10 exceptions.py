# 1 Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом,
# то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введенные числа суммируются.
"""value_1 = input()
value_2 = input()
try:
    print(int(value_1) + int(value_2))
except:
    print(str(value_1) + str(value_2))"""

# 2 Напишите программу для проверки валидности номера телефона.
# Главный критерий: номер может содержать в себе только целые числа.
"""phone_number = input("Input your phone number\n")
try:
    print("We will contact you by phone number:", int(phone_number))
except:
    print("Phone number can contain only digits!")"""

# 3 Напишите программу которая запрашивает числа пока мы не введем 0. Все введенные числа кроме 0 должны записываться в массив.
# После программа запрашивает ввести целое число как индекс. Если в списке есть элемент с введенным индексом,
# программа выведет данный элемент,  если нет, выведет “There is no such element”.
"""arr = []
while True:
    value = input()
    if value == "0":
        break
    try:
        arr.append(int(value))
    except:
        continue

index = input(">")
try:
    print(arr[int(index)])
except:
    print("There is no such element")"""

# 4
"""class Book:
    number = int()
    title = str()
    author = str()
    pages = int()
    
    def __init__(self, b_num, b_title, b_author, b_pages):
        self.number = b_num
        self.title = b_title
        self.author = b_author
        self.pages = b_pages
        
    def getData(self):
        print("number - {0}, title - {1}, author - {2}, pages - {3}"
              .format(self.number, self.title, self.author, self.pages))


b1 = Book(1, "Harry Potter", "Rowling", 3000)
b2 = None
b3 = Book(3, "Lord of the rings", "J.R.R.Tolkien", 9001)
b4 = Book(4, "The witcher", "A.Sapkovsky", 5000)
b5 = Book(5, "jsbdkjdsbg", "jkagfbfjgb", 3)
library = [b3, b2, b1, b4, b5]

for i in library:
    try:
        i.getData()
    except:
        print("Book is empty")"""

# 5
class User:
    name = str()
    surname = str()
    age = int()

    def __init__(self, u_name, u_surname, u_age):
        self.name = u_name
        self.surname = u_surname
        self.age = u_age


class Main:
    arr = []
    for i in range(2):
        name = input()
        surname = input()
        age = input()


        try:
            if int(age) < 0:
                a="dsaf"
                print(int(a))
            user = User(name, surname, int(age))
            arr.append(user)
        except:
            user = User(name, surname, 0)
            arr.append(user)

    sum_age = 0
    for k in arr:
        sum_age += k.age
        print((k.age, sum_age))
    mean_age = sum_age / len(arr) if len(arr) != 0 else 0
    print(mean_age)