#1 Создайте двумерный массив и заполните значениями – [[12,5,7,6],[4,0,2,7],[9,1,3,2],[10,-2,4,6]].
# С консоли примите два числа N и M, и покажите на экране значение которое хранится по этому индексу
"""arr=[[12,5,7,6],
    [4,0,2,7],
    [9,1,3,2],
    [10,-2,4,6]]
n=int(input("n="))
m=int(input("m="))
print(arr[n][m])"""
#2 Создайте двумерный массив размером 2xN из целых чисел и с помощью цикла выведите элементы каждого
# одномерного массива в отдельной строке
"""n=int(input())
arr=[int(i) for i in input().split()]
first_row=[arr[i] for i in range(n)]
second_row=[arr[i] for i in range(n, n*2)]
solution=[first_row, second_row]
for i in solution:
    print(i)"""
#3 Напишите программу в котором я ввожу два числа N и M. Затем создаю двумерный массив NxM.
# Далее мы заполняем этот массив числами. После заполнения программа запрашивает число K и показывает элементы только этой строки
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for i in range(m):
        row[i]=int(row[i])
    arr.append(row)
k=int(input())
for j in arr[k]:
    print(j, end=" ")"""
#4 Напишите программу в котором я ввожу два числа N и M. Затем создаю двумерный массив NxM.
# Далее мы заполняем этот массив числами. После заполнения программа должна показать элементы строк индексы которых четные
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for i in range(m):
        row[i]=int(row[i])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i%2==0:
            print(arr[i][j], end=' ')
    print()"""
#5 Программа запрашивает два числа N и М, затем создает двумерный массив размером NxM.
# Пользователь заполняет массив значениями, после чего программа должна показать только четные элементы массива
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for i in range(m):
        row[i]=int(row[i])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]%2==0:
            print(arr[i][j], end=" ")
    print()"""
#6 Создайте программу которая принимает массив с размером NxM со значениями и показывает только положительные элементы в нем
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for i in range(m):
        row[i]=int(row[i])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]>0:
            print(arr[i][j], end=" ")
    print()"""
#7 Из массива размером NxM программа должна показывать только четные и положительные элементы
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for i in range(m):
        row[i]=int(row[i])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]>0 and arr[i][j]%2==0:
            print(arr[i][j], end=" ")
    print()"""
#8 Напишите программу которая принимает значения в двумерный массив размером NxM и показывает квадраты всех элементов
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for j in range(m):
        row[j]=int(row[j])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j]**2, end=" ")
    print()"""
#9 Программа должна напечатать индексы отрицательных чисел двумерного массива размеров NxM
"""n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=input().split()
    for j in range(m):
        row[j]=int(row[j])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]<0:
            print(i,j)"""

# 10 Создайте программу которая принимает значения для массива размером NxM и находит сумму всех его элементов, имеющих оба четных индекса
"""n = int(input())
m = int(input())
arr = []
sum_ = 0
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i % 2 == 0 and j % 2 == 0:
            sum_ += arr[i][j]
print(sum_)"""
# 11 Выведите сумму элементов каждой строки двумерного массива размером NxM. Размер и значения задаются с консоли
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
sum_ = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum_ += arr[i][j]
    print(sum_)
    sum_ = 0"""

# 12 Напишите программу которая находит и выводит максимальное значение в двумерном массиве, а также выводит его индекс
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
max_ = None
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if max_ is None or arr[i][j] >= max_:
            max_ = arr[i][j]
            i_max = i
            j_max = j
print(max_)
print(i_max, j_max)"""

# 13 Программа должна заменить все нечетные элементы двумерного массива на 0 и вывести результат на экран
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] % 2 != 0:
            arr[i][j] = 0
        print(arr[i][j], end=" ")
    print()"""

# 14 Ваша программа должна находить в двумерном массиве минимальный и максимальный элементы, затем поменять их местами в массиве
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
max_ = None
min_ = None
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if max_ is None or arr[i][j] >= max_:
            max_ = arr[i][j]
            i_max = i
            j_max = j
            #print(max_)
        if min_ is None or arr[i][j] <= min_:
            min_ = arr[i][j]
            i_min = i
            j_min = j
            #print(min_)
# пачиму низя max(arr) min(arr), так многакода (
arr[i_max][j_max] = min_
arr[i_min][j_min] = max_
# если есть несколько одинаковых макс или мин, заменяет только одно

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()"""

# 15 Напишите программу которая принимает значения в двумерный массив размером NxM, а также некое число k.
# Если элемент массива делится на k без остатка, программа должна заменить этот элемент на результат деления этого числа на k
"""n = int(input("n="))
m = int(input("m="))
k = int(input("k="))
arr = []
for i in range(n):
    row = input(">split ").split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] % k == 0:
            arr[i][j] = arr[i][j] / k
        print(round(arr[i][j]), end=" ")
    print()"""

# 16 Напишите программу в котором я ввожу два числа N и M. Затем создаю двумерный массив NxM. Далее мы заполняем
# этот массив числами. Программа должна вывести максимальный элемент в каждой строке.
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)

for i in range(len(arr)):
    max_ = None
    for j in range(len(arr[i])):
        if max_ is None or arr[i][j] >= max_:
            max_ = arr[i][j]
    print(max_)"""

# 17 Напишите программу в котором я ввожу два числа N и M. Затем создаю двумерный массив NxM.
# Далее мы заполняем этот массив числами. Программа должна вывести максимальный элемент в каждом столбце.
"""n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)

for i in range(len(arr[i])):
    print(max([row[i] for row in arr]))"""

# 18 Программа запрашивает число N, затем мы создаем двумерный массив N x N и заполняем их числами.
# Программа должна заменить первую нулевую строку массива на последнюю строку массива.
"""n = int(input())
arr = []
for i in range(n):
    row = input().split(maxsplit=n)[:n]
    for i in range(n):
        row[i] = int(row[i])
    arr.append(row)
arr[0], arr[n-1] = arr[n-1], arr[0]
for row in arr:
    print(' '.join([str(elem) for elem in row]))"""

# 19 Программа запрашивает заполнить числами двумерный массив размером NxM, затем заменяет на 0 те элементы
# которые меньше среднего значения всех элементов данной строки
while True:
    n = int(input("n="))
    m = int(input("m="))
    if (n, m) > (0, 0):
        break
arr = []
sumo = []
for i in range(n):
    row = input("> ").split(maxsplit=m)[:m]
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)

for i in range(len(arr)):
    sum = 0
    for j in range(len(arr[i])):
        sum += arr[i][j]
    sumo.append(sum)

for c in range(n):
    index = -1
    for change in arr[c]:
        index += 1
        if change < sumo[c] / m:
            arr[c][index] = 0

for row in arr:
    print(' '.join([str(elem) for elem in row]))

# 20 Программа должна найти минимальный элемент среди максимальных элементов каждой строки двумерного массива
"""n = int(input())
m = int(input())
arr = []
arr2 = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)

for i in range(len(arr)):
    max_ = None
    for j in range(len(arr[i])):
        if max_ is None or arr[i][j] >= max_:
            max_ = arr[i][j]
    arr2.append(max_)
print(max(arr2))"""
