#1 Дан кортеж: t = (10, 20, 30, 40, 50, 60)
#Напишите программу, чтобы вывести кортеж в обратном порядке
"""t = (10, 20, 30, 40, 50, 60)
for i in range(len(t)):
    print(t[len(t)-i-1],end=" ")"""
#2 Даны два кортежа: a = (12, 14), b = (28, 30).
#Напишите программу, чтобы поменять значения местами.
"""a = (12, 14)
b = (28, 30)
a,b=(28,30),(12,14)
print("a = ",a)
print("b = ",b)"""
#3 Напишите программу, где мы вводим 4 числа и сохраняем их в кортеж.
# Нужно проверить равны ли все элементы в кортеже. Если все элементы равны, выведете EQUAL, иначе NOT EQUAL.
"""a=int(input())
b=int(input())
c=int(input())
d=int(input())
arr=(a,b,c,d)
if arr[0]==arr[1]==arr[2]==arr[3]:
    print("EQUAL")
else:
    print("NOT EQUAL")"""
#4 Дан кортеж t = ("apple", "banana", 123, "melon")
#Напишите программу, чтобы поменять значение 123 на значение lemon.
"""t = ("apple", "banana", 123, "melon")
t=list(t)
t[2]="lemon"
t=tuple(t)
print(t)"""
#5 Дан кортеж t = ("apple", "banana", "lemon", "melon")
#Напишите программу которая принимает строку и проверяет есть ли данная строка внутри кортежа. Если есть, выводим EXISTS, иначе  NOT EXISTS.
"""t = ("apple", "banana", "lemon", "melon")
p=str(input())
print("EXISTS" if p in t else "NOT EXISTS")"""
#6 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Нужно с помощью цикла вывести все элементы.
"""n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
for d in arr:
    print(d)"""
#7 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Нужно с помощью цикла вывести все элементы вместе с индексами.
"""n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
for d in range(n):
    print(d,"-",arr[d])"""
#8 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Выведите в конце квадраты всех введенных чисел.
"""n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
for c in arr:
    print(c**2,end=" ")"""
#9 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Выведите в конце все элементы в обратном порядке.
"""n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
for c in range(len(arr)):
    print(arr[len(arr)-c-1],end=" ")"""
#19 Напишите программу которая прописывает каждое слово в тексте в обратном порядке.
text=input().split()
for i in text:
    word=i
    ans=""
    for j in range(len(word)):
        ans = ans + word[len(word)-j-1]
    print(ans, end=" ")





