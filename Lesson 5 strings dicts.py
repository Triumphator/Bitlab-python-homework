#1 Напишите программу которая принимает текст и выводит длину(количество символов) текста на экран.
"""text=str(input())
print(len(text))"""
#2Программа должна запрашивать текст и выводить на экран первый символ(букву) текста.
from typing import Tuple

"""text=str(input())
print(text[0])"""
#3 Принимайте с консоли некий текст и сравните его со словом "BITLAB".
# Если они абсолютно идентичны, выведите на  экран "YES", иначе "NO".
"""text=str(input())
print("YES" if text=="BITLAB" else "NO")"""
#4 Напишите программу которая принимает текст и сранивает его со словом "python".
# Если они равны без учета регистров (заглавные и строчные буквы) выведите "YES", иначе "NO"
"""text=str.lower(input())
print("YES" if text=='python' else "NO")"""
#5 Программа запрашивает два слова и сравнивает их без учета регистров (заглавные и строчные буквы).
# Выведите на экран "THEY ARE EQUAL" если оны равны, и "THEY ARE NOT EQUAL" в противном случае.
"""
textOne=str.lower(input())
textTwo=str.lower(input())
print("THEY ARE EQUAL" if textOne==textTwo \
      else "THEY ARE NOT EQUAL")"""
#6 Напишите программу которая принимает одно слово и одну букву. Выведите индекс буквы в слове если она там
# присутствует, и "THERE IS NO SUCH LETTER" если в слове буквы не окажется.
"""text=str(input())
letter=str(input())
check=None
for i in range(len(text)):
    if text[i]==letter:
        print(i, end=" ")
        check=True
if check is not True:
    print("THERE IS NO SUCH LETTER")"""
#7 Напишите программу которая принимает слово и выводит каждый символ этого слова в отдельной строке.
"""text=str(input())
for i in range(len(text)):
    print(text[i])"""
#8 Напишите программу, которая продублирует все символы введенного текста.
"""text=str(input())
for i in text:
    print(i*2, end="")"""
#9 Программа должна принимать текст и букву, затем подсчитать сколько раз буква встречается в тексте.
"""text=str(input()).lower()
letter=str(input()).lower()
count=0
for i in text:
    if i==letter:
        count+=1
print(count)"""
#10 Напишите программу которая показывает принятый текст в обратном порядке.
"""text=str(input())
for i in range(len(text)):
    print(text[len(text) - i - 1], end = '')"""
#11 Вводим в программу две строки s1 и s2.
# Если s2 содержится внутри слова s1, то программа выводит "Yes", иначе "No".
"""s1=input(); s2=input()
print("Yes" if s2 in s1 else "No")"""
#12 Мы вводим строку (текст) в нашу программу.
# Программа должна вывести количество гласных букв. (Гласные буквы: a, e, i, o, u)
"""text=input()
vowels=0
for letter in text:
    if letter in "aeiouAEIOU":
        vowels = vowels+1
print(vowels)"""
#13 Напишите программу которая выводит сумму всех цифр в тексте.
"""text=input()
numsum=0
for i in range(len(text)):
    if text[i].isdigit():
        numsum+=int(text[i])
print(numsum)"""
#14 Вводим строки s1 и s2 в программу.
# Программа должна вывести "YES", если s2 является противоположным (в обратном чтении) s1. Иначе "NO".
"""s1=input().lower(); s2=input().lower(); s2reverse=""
for i in range(len(s2)):
    s2reverse+=(s2[len(s2)-i-1])
print("Yes" if s1==s2reverse else "No")"""
#16 Сделайте некое подобие калькулятора который принимает два числа
# и оператор(+, -, *, /) между ними в виде текста. Выведите на экран результат операции.
"""text=input("x+y, x-y, x*y, x/y\ny must be positive number\nx can be negative\n")
oper=None
for i in text:
    if i.isdigit()==False:
        oper=i
x=text.partition(oper)

if oper=="+":
    print(int(x[0]) + int(x[2]))
elif oper=="-":
    print(int(x[0]) - int(x[2]))
elif oper=="*":
    print(int(x[0]) * int(x[2]))
elif oper=="/":
    if x[2]!="0":
        print(int(x[0]) / int(x[2]))
    else:
        print("Cannot divide by 0")
else:
    print("Incorrect string")"""



"""from operator import truediv, mul, add, sub

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def calculate(s):
    if s.isdigit(): # If s.isdigit() is True, that means the user only input a number, no operators, and so the program will only return that number
        return float(s)
    for c in operators.keys(): # For every key in the operators dictionary...
        left, operator, right = s.partition(c) # splitting the string at the operator to get a tuple: ('34','+','54')
        if operator in operators: # If the operator is in operators:
            return operators[operator](calculate(left), calculate(right)) # Call the value(function imported) for that key with the arguments, left (34) and right (54)

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))"""

#17 Напишите программу, которая преобразует все заглавные символы строки в нижний регистр.
"""text=input()
print(text.swapcase())"""
#18 Напишите программу которая переписывает текст так чтобы каждое слово начиналось с заглавной буквы.
"""text=input().title()
print(text)"""
#19 Напишите программу которая прописывает каждое слово в тексте в обратном порядке.
"""text=input()
for i in range(len(text)):
    print(text[len(text) - i - 1], end = '')"""
#20 Напишите программу которая принимает длинный текст(String text) и два отдельных слова (String S1 и String S2).
# Программа должна заменить первое слово(S1) везде где оно встречается на второе слово (S2).
"""String_text=input()
String_S1=input()
String_S2=input()
if String_S1 in String_text:
    print(String_text.replace(String_S1,String_S2))
else:
    print(String_S1 + " is not found in text")"""
#21 Программа запрашивает число N, создайте словарь в котором ключи и значения будут храниться в виде (N, N*N)
"""n=int(input())
arr={n:n*n for n in range(1,n+1)}
print(arr)"""
#22 Программа запрашивает логин и пароль пользователя. Если в словаре users(ключ - логин, и значение - пароль)
# логин совпадает с паролем, вывести Authentication completed, иначе Incorrect login or password.

"""users = {
    "user": "qwerty", "user2": "qwerty2", "user3": "qwerty3"
  }
login=input("Login: ")
password=input("Password: ")
if users.get(login)==password:
    print("Authentication completed")
else:
    print("Incorrect login or password")"""
#23 Создайте словарь, состоящий из пар синонимов. В консоли вы вводите количество слов, слова-синонимы и слово, а программа возвращает вам синоним.
"""synonyms={}
n=int(input("Enter number of words you want to add \n"))
for i in range(n):
    word=input("Word - ")
    synonyms[word]=input("Synonym of "+word+" - ")
request=input("Search for synonym of ")
print(synonyms.get(request))"""
#24 В словаре employee поменяйте зарплату сотрудника John на 300000.
employee = {
'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
    }
employee['employee3']={'name': 'John', 'age': 25, 'salary': 300000}
print(employee)
