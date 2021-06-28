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
