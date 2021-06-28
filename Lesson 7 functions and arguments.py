# 1 Напишите функцию, которая в аргументы принимает 3 значения целостных чисел, и возвращает самую максимальную из них.
"""def max_(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input())
b = int(input())
c = int(input())
print(max_(a,b,c))"""

# 2 Напишите функцию, которая в аргументы принимает три натуральных числа a, b, c.
# Определите, существует ли треугольник с такими сторонами.
# # Если треугольник существует, выведите строку YES, иначе выведите строку NO.
"""def triangle(a,b,c):
    triangle=a+b>c and b+c>a and a+c>b
    if triangle:
        print("YES")
    else:
        print("NO")
a = int(input())
b = int(input())
c = int(input())
triangle(a,b,c)"""

# 3 Напишите функцию, которая проверяет, делится ли число на 2 без остатка или нет.
"""def even(a):
    if a % 2 == 0:
        print("YES")
    else:
        print("NO")
a=int(input())
even(a)"""

# 4 Напишите функцию, которая в аргументы принимает строку и продублирует все символы.
"""def double():
    text = str(input())
    for i in text:
        print(i * 2, end="")
double()"""

# 5 Напишите функцию, которая в аргументы принимает строку и букву.
# Нужно посчитать сколько раз буква встречается в тексте. (Без учета регистра)
"""def letter_search():
    text = str(input()).lower()
    letter = str(input()).lower()
    count = 0
    for i in text:
        if i == letter:
            count += 1
    print(count)
letter_search()"""

# 6 Напишите функцию, которая в аргументы принимает строку.
# Нужно посчитать количество гласных букв в строке. (Гласные буквы: a, e, i, o, u)
"""def vowels(text):
    vowels = 0
    for letter in text:
        if letter in "aeiouAEIOU":
            vowels = vowels + 1
    print(vowels)
vowels("oblako")"""

# 7 Напишите функцию, которая в аргументы принимает строку. Нужно определить, является ли наша строка палиндромом или нет.
# Палиндром - это когда текст читается так же одинаково если ее читать в обратном порядке.
"""def palindrome(text):
    text_reverse = ""
    for i in range(len(text)):
        text_reverse += (text[len(text) -i -1])
    print ("YES" if text == text_reverse else "NO")

text = str(input())
palindrome(text)"""

# 8 Напишите функцию, которая в аргументы принимает две строки s1 и s2.
# Если s2 содержится внутри слова s1, то программа выводит "YES", иначе "NO".
"""def inside(s1, s2):
    print("YES" if s2 in s1 else "NO")
s1 = str(input())
s2 = str(input())
inside(s1, s2)"""

# 9 Напишите функцию, которая принимает в аргументах массив
# целостных чисел, в итоге программа должна вывести количество элементов не равных 0.
"""def even_array(args):
    count = 0
    for i in args:
        i = int(i)
        if i != 0:
            count += 1
    print(count)
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
even_array(arr)"""

# 10 Создайте такую функцию, которая принимает в аргументы массив целостных чисел.
# Функция должна вывести на экран уникальные элементы массива.
"""def unique(array):
    for i in range(len(array)):
        flag = True
        for j in range(len(array)):
            if i == j:
                continue
            elif array[i] == array[j]:
                flag = False
                break
        if flag == True:
            print(array[i])

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

unique(arr)"""

# 11
"""def authentication(login,password):
    if login == "admin" and password == "qwerty":
        print("Authentication completed")
    else:
        print("Invalid password")

login=input()
password=input()
authentication(login,password)"""

# 12 Создайте такую функцию, которая принимает в аргументы массив целостных чисел.
# Выведите минимальный элемент и максимальный элемент массива.
"""def minmax(array):
    print("min:", min(array))
    print("max:", max(array))

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
minmax(arr)"""

# 13 Создайте такую функцию, которая принимает в аргументы массив целостных чисел.
# Программа должна вывести среднее арифметическое всех четных элементов массива.
"""def mean_even(array):
    sum = 0
    count = 0
    for i in array:
        if i%2 == 0:
            sum += i
            count += 1
            print(sum)
    print(round(sum/count) if count != 0 else "No even numbers")

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

mean_even(arr)"""

# 14 Создайте такую функцию, которая принимает в аргументы 2 целостных чисел a и b, также знак оператора.
# Программа должна вывести результат исходя от  арифметического оператора.
"""def calc(a,b,oper):
    if oper in "+-*/":
        if oper == "+":
            print(a+b)
        elif oper == "-":
            print(a-b)
        elif oper == "/":
            print(a/b if b !=0 else "Cannot divide by 0")
        else:
            print(a*b)
    else:
        print("Incorrect operator")

a = int(input())
b = int(input())
oper = input()

calc(a,b,oper)
"""
# 15 Создайте такую функцию, которая принимает в аргументы двумерный массив размера NxN.
# Замените первую горизонтальную половину на вторую горизонтальную половину.
"""def swap_rows(arr):
    arr[0], arr[- 1] = arr[- 1], arr[0]
    for row in arr:
        print(' '.join([str(elem) for elem in row]))

n = int(input())
arr = []
for i in range(n):
    row = input().split(maxsplit=n)[:n]
    for i in range(n):
        row[i] = int(row[i])
    arr.append(row)

swap_rows(arr)"""

# 16 Создайте такую функцию, которая принимает в аргументы двумерный массив размера NxM.
# Программа должна вывести максимальный элемент в каждой строке.
"""def max_row(arr):
    for i in range(len(arr)):
        max_ = None
        for j in range(len(arr[i])):
            if max_ is None or arr[i][j] >= max_:
                max_ = arr[i][j]
        print(max_)

n = int(input())
m = int(input())
arr = []
for i in range(n):
    row = input().split(maxsplit=m)[:m]
    for j in range(m):
        row[j] = int(row[j])
    arr.append(row)

max_row(arr)"""

# 17 Создайте такую функцию, которая принимает в аргументы массив из целых чисел.
# Программа должна выводить нечетные числа из массива и остановиться, если встретит число 23.
"""def odd_array(array):
    for i in array:
        if i == 23:
            break
        elif i %2 != 0:
            print(i)

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

odd_array(arr)"""

# 18 Создайте такую функцию, которая принимает в аргументы массив из целых чисел.
# Необходимо вывести элементы, которые одновременно меньше 50 и делятся на 5 без остатка.
"""def less_50(array):
    for i in array:
        if i < 50 and i %5 == 0:
            print(i)

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

less_50(arr)"""

# 19 Создайте такую функцию, которая принимает в аргументы массив из целых чисел.
# Необходимо просуммировать элементы массива не учитывая элементы которые делятся на 5 без остатка.
"""def sum_array(array):
    sum = 0
    for i in array:
        if i %5 == 0:
            sum += i
    print(sum)

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

sum_array(arr)"""

# 20 Создайте такую функцию, которая принимает в аргументы номер месяца и возвращает название сезона.
# (Winter, Spring, Summer, Autumn)
"""def seasons(month):
    if 1<= month <= 12:
        if 3 <= month <= 5:
            print("Spring")
        elif 6 <= month <= 8:
            print("Summer")
        elif 9 <= month <= 11:
            print("Autumn")
        else:
            print("Winter")

month_number = int(input())

seasons(month_number)"""

# 21 Создайте такую функцию, которая принимает в аргументы список целостных чисел.
# Нужно отсортировать список по возрастанию.
"""def array_sort(array):
    array.sort()
    for i in array:
        print(i, end=" ")
    #print(sorted(array))

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

array_sort(arr)"""

# 22 Создайте такую функцию, которая принимает в аргументы список из строк и строку s.
# Определите, содержит ли список данную строку s. Если содержит вывести Yes, иначе No.
"""def string_list(list, string):
    condition = False
    for i in list:
        if i == string:
            condition = True
    print("Yes" if condition else "No")

n = int(input())
arr = []
for i in range(n):
    x = input().split(maxsplit=n)[:n]
    arr.append(x)
s = input()

string_list(arr, s)"""

# 23 Создайте такую функцию, которая принимает в аргументы двумерный массив размера NxN.
# Выведите все элементы стоящие на диагонали как показано в примерах.