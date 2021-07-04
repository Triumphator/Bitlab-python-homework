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

# 10 Создайте массив из целых чисел и с помощью цикла выведите все элементы с четными индексами.
"""n=int(input())
arr=[]
index=-1
for i in range(n):
    x = int(input())
    arr.append(x)
for even in arr:
    index+=1
    if index%2==0:
        print(even, end=" ")"""
# 11 Создайте массив из целых чисел и с помощью цикла выведите все элементы с нечетными индексами.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
index=-1
for i in range(n):
    x = int(input())
    arr.append(x)
for odd in arr:
    index+=1
    if index%2!=0:
        print(odd, end=" ")"""
# 12 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Вывести все содержащиеся в данном массиве четные числа.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
for number in arr:
    if number%2==0:
        print(number, end=" ")"""
# 13 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце только положительные элементы.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
for number in arr:
    if number>0:
        print(number, end=" ")"""
# 14 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце количество положительных элементов.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
PositiveNumberCount=0
for number in arr:
    if number>0:
        PositiveNumberCount+=1
print(PositiveNumberCount)"""
# 15 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце сумму всех элементов массива.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=0
for number in arr:
    numsum=numsum+number
print(numsum)"""
# 16 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце максимальный элемент и его индекс.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
index=-1
maxNumber=None
maxIndex=None
for number in arr:
    index+=1
    if maxNumber is None:
        maxNumber=number
    if number>=maxNumber:
        maxNumber=number
        maxIndex=index
print(maxNumber,maxIndex)"""
# 17 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Программа должна вывести умножение всех элементов, не равных 0.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
multiply=1
for number in arr:
    if number!=0:
        multiply=number*multiply
print(multiply)"""
# 18 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Программа должна вывести сумму и среднее значение введенных чисел.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=0
for number in arr:
    numsum=numsum+number
mean=numsum/len(arr)
print(numsum,mean)"""
# 19 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце минимальный элемент и максимальный элемент массива.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
print(min(arr),max(arr))"""
# 20 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив. Выведите в конце разность между максимальным и минимальными элементами.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
print(max(arr)-min(arr))"""
# 21 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Программа должна вывести сумму и среднее значение исключая максимальное и минимальное значение.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=0; maxnumber=None; minnumber=None
for number in arr:
    if maxnumber is None and minnumber is None:
        maxnumber,minnumber=number,number
    if number>=maxnumber:
        maxnumber=number
    if number<=minnumber:
        minnumber=number
    numsum=numsum+number
numsum=numsum-minnumber-maxnumber
mean=numsum/(len(arr)-2)
print(numsum,mean)"""
# 22 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Программа должна заменить местами максимальный и минимальный элементы.
"""while True:
    n=int(input())
    if n>0:
        break
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
index=-1; maxindex=0; minindex=0; maxnumber=None; minnumber=None
for number in arr:
    if maxnumber is None and minnumber is None:
        maxnumber,minnumber=number,number
    index+=1
    if number>=maxnumber:
        maxnumber=number
        maxindex=index
    if number<=minnumber:
        minnumber=number
        minindex=index
arr[maxindex]=minnumber
arr[minindex]=maxnumber
for d in arr:
    print(d, end=" ")"""
# 23 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Далее, программа запрашивает пользователя число m. Если число m существует в нашем массиве, программа должна
# вывести слово "YES" и вывести индекс (расположение, адрес) данного числа. Иначе вывести слово "NO".
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
m = int(input("Enter a number to check if it's in list "))
for num in arr:
    if num == m:
        print("YES", arr.index(m))
        break
else:
    print("NO")"""
#24 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Выведите в конце среднее арифметическое отрицательных элементов массива.
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=0; count=0
for d in arr:
    if d<0:
        numsum=numsum+d
        count+=1
print(numsum/count if count>0 else "No negative numbers in list")"""
#25 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Выведите в конце элементы массива, которые больше среднего арифметического.
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=0
for d in arr:
    numsum=numsum+d
mean=numsum/len(arr)
for number in arr:
    if number>mean:
        print(number, end=" ")"""
#26 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Затем мы вводим число m. Программа должна вывести среднее значение всех элементов, которые больше m.
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
m=int(input("m="))
moreMsum=0; count=0; mean=None
for k in arr:
    if k>m:
        moreMsum=moreMsum+k
        count+=1
if count>0:
    mean=moreMsum/count
print(round(mean,1) if count>0 else "No numbers are bigger than 'm'")"""
#27 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Программа должна вывести среднее арифметическое всех четных элементов массива. (Число 0 тоже четный элемент)
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
even=0; count=0; mean=None
for d in arr:
    if d%2==0:
        even=even+d
        count+=1
if count!=0:
    mean=even/count
print(round(mean,1) if mean is not None else "All numbers are odd")"""
#28 Напишите программу которая запрашивает числа пока мы не введем 0.
# Все введенные числа кроме 0 должны записываться в массив. В итоге выведите только положительные элементы.
"""arr=[]
while True:
    n=int(input("Enter 0 to stop "))
    if n==0:
        break
    arr.append(n)
if arr:
    for i in arr:
        if i>0:
            print(i, end=" ")
else:
    print("Your list is empty")"""
#29 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Программа должна вывести сумму всех чисел которые находятся между нулями.
"""while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
numsum=None; stop=0
for k in arr:
    if k==0:
        stop+=1
        if stop==2:
            break
        numsum=0
    if numsum is not None:
        numsum = numsum + k
print(numsum)"""
#30 Программа запрашивает число n. Далее, мы вводим n чисел и сохраняем все введенные числа в массив.
# Затем программа запрашивает число k. Вывести все числа в массиве, которые делятся на k без остатка.
while True:
    n = int(input("Enter list length "))
    if n > 0:
        break
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
while True:
    k=int(input("k="))
    if k>0:
        break
for f in arr:
    if f%k==0:
        print(f, end=" ")








