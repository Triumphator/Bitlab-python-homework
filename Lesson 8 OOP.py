# 2 Создайте 5 объектов из класса Phone которую мы объявили выше. Задайте им разные значения (name, model, price).
# Затем, выведите на консоль данные о каждом телефоне при помощи метода getData().
"""class Phone:
    name = ""
    model = ""
    price = ""

    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def getData(self):
        print("name = {0}, model = {1}, price = {2}".format(self.name,self.model,self.price))

arr = []
iPhone12 = Phone("iPhone","12",200);    arr.append(iPhone12)
redMi = Phone("RedMi Note Pro", 8, 100);    arr.append(redMi)
nokia = Phone("Nokia", "nGage", 50);    arr.append(nokia)
huawei = Phone("Huawei", "1", 120);     arr.append(huawei)
siemens = Phone("Siemens","N71",23);    arr.append(siemens)

for phone in arr:
    phone.getData()"""

# 4 Создайте массив из класса Student, заполните массив 5 объектами класса Student которые мы
# создали до этого, и используя цикл, выведите данные по каждому студенту.
"""class Student:
    id = int()
    name = ""
    surname = ""
    gpa = float()

    def __init__(self, id, name, surname, gpa):
        self.id = id
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def getStudentData(self):
        print("id = {0}, name = {1}, surname = {2}, gpa = {3}".format(self.id,self.name,self.surname,self.gpa))

    def topStudent(students):
        mx = students[0]
        for person in students:
            if mx.gpa < person.gpa:
                mx = person
        print(mx.name, mx.surnam, mx.gpa)


class Main:
    student_Jaina = Student(1, "Jaina", "Proudmoore", 5.4)
    student_Arthas = Student(2, "Arthas", "Menethil", 3.4)
    student_Quel = Student(3, "Quel-Thas", "Sunstrider", 4.5)
    student_Sylva = Student(4, "Sylvanas", "Windrunner", 2.9)
    student_Tirion = Student(5, "Tirion", "Fordring", 3.8)
    student_Alleria = Student(6, "Alleria", "Windrunner", 1.2)
    student_Vereesa = Student(7, "Vereesa", "Windrunner", 1.8)
    student_Garrosh = Student(8, "Garrosh", "Hellscream", 0.1)
    student

    students = []
    students.append(student_Jaina)
    students.append(student_Arthas)
    students.append(student_Quel)
    students.append(student_Sylva)
    students.append(student_Tirion)"""

# 6
# noinspection PyGlobalUndefined
"""class Student:
    name = str()
    surname = str()
    gpa = float()


    def __init__(self, s_name, s_surname, s_gpa):
        self.name = s_name
        self.surname = s_surname
        self.gpa = s_gpa

    def getStudentData(self):
        print("{0}, {1}, {2}".format(self.name,self.surname,self.gpa))
        
    def add_student(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.gpa = gpa
        students_list.append(Student(name, surname, gpa))
        


students_list = []

while True:
    n = int(input("PRESS [1] TO ADD STUDENT\n"
                  "PRESS [2] TO LIST STUDENTS\n"
                  "PRESS [0] TO EXIT\n"))
    if 0 <= n <= 2:
        if n == 1:
            name = str(input("Insert name?\n"))
            surname = str(input("Insert surname?\n"))
            gpa = float(input("Insert gpa?\n"))
            Student.add_student(name,surname,gpa)
            continue
        elif n == 2:
            for i in range(len(students_list)):
                print(i+1,")", end= " "); (students_list[i].getStudentData())
            continue
        else:
            print("Exiting")
            break"""

# 7
class Employee:
    name = str()
    age = int()
    salary = str()

    def __init__(self, e_name, e_age, e_salary):
        self.name = e_name
        self.age = e_age
        self.salary = e_salary

    def printData(self):
        print("name - {0}, age - {1}, salary - {2}".format(self.name, self.age, self.salary))


class Programmer(Employee):
    programming_language = str()

    def __init__(self, e_name, e_age, e_salary, p_lang):
        super().__init__(self, e_name, e_age, e_salary)
        self.programming_language = p_lang

    def printData(self):
        print("name - {0}, age - {1}, salary - {2},"
              "programming language - {3}".format(self.name, self.age, self.salary, self.programming_language))

class DataAnalyst(Employee):
    databaseTool = str()

    def __init__(self, e_name, e_age, e_salary, dbTool):
        super().__init__(self, e_name, e_age, e_salary)
        self.databaseTool = str()

    def printData(self):
        print("name - {0}, age - {1}, salary - {2},"
              "database tool - {3}".format(self.name, self.age, self.salary, self.databaseTool))


class Main:
    daJaina = DataAnalyst("Jaina", 28, 9032, "Frost magic")
    daKael = DataAnalyst("Kael'Thas", 35, 8065, "Arcane magic")
    daSylva = DataAnalyst("Sylvanas", 31, 7403, "Banshee powers")
    prArthas = Programmer("Arthas", 28, 6666, "Frostmourne")
    prGarrosh = Programmer("Garrosh", 29, 4600, "Axe")
    prTirion = Programmer("Tirion", 35, 5400, "Ashbringer")

    employees = [daJaina, daKael, daSylva, prTirion, prGarrosh, prArthas]

    for i in employees:
        i.printData()

    sum_sal = 0
    for k in employees:
        sum_sal += k.salary
    mean_salary = sum_sal/len(employees)
    print(mean_salary)

# 8
class User:
    id = int()
    login = str()
    password = str()
    name = str()
    surname = str()

    def __init__(self, u_id, u_login, u_password, u_name, u_surname):
        self.id = u_id
        self.login = u_login
        self.password = u_password
        self.name = u_name
        self.surname = u_surname

    def getData(self):
        print("id - {0}, name - {1}, surname - {2}, login - {3}, password - {4}"
              .format(self.id, self.name, self.surname, self.login, self.password))


class Staff(User):
    salary = float()
    subjects = []

    def __init__(self, u_id, u_login, u_password, u_name, u_surname, s_salary):
        super(Staff, self).__init__(s_salary)
        self.salary = s_salary

    def getData(self):
        print("id - {0}, name - {1}, surname - {2}, login - {3}, password - {4}, salary - {5}"
              .format(self.id, self.name, self.surname, self.login, self.password, self.salary))

    def addSubject(self, subject):
        subjects.append(subject)
