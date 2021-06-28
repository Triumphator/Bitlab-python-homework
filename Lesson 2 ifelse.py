#1
"""a=int(input())
b=int(input())
print (a if a>b else b)"""
#2 пишите программу, где ввожу число n, и если оно между 10 и 20, то программа выведет YES иначе NO.
"""n=int(input("Enter a number "))
print("YES" if n>10 and n<20 else "NO")"""
#3 ишите программу, где ввожу целое число n, и если оно четное, программа выведет EVE
"""n=int(input("Enter a number "))
print("EVEN" if n%2==0 else "ODD")"""
#4 ано число. Если оно меньше или равно 2019, то вывести NO, если больше или равно 2021, то вывести YES, если равно 2020, то вывести Error.
"""n=int(input("Enter a number "))
if n<=2019:
    print("NO")
elif n>=2021:
    print("YES")
else:
    print("Error")"""
#5 апишите программу, где ввожу номер дня недели(1-7). Выведите название дня недел
"""d=int(input("Enter a number between 1-7 "))
if d==1:
    print("Monday")
elif d==2:
    print("Tuesday")
elif d==3:
    print("Wednesday")
elif d==4:
    print("Thursday")
elif d==5:
    print("Friday")
elif d==6:
    print("Saturday")
elif d==7:
    print("Sunday")
else:
    print("Wrong number")"""
#6 пишите программу, где ввожу целое число. Если оно больше 100 или меньше -100, то меняем значение переменной на 0, иначе увеличьте его на 1.
"""n=int(input("Enter a solid number "))
if n>100 or n<-100:
    n=0
else:
    n=n+1
print(n)"""
#7 пишите программу, где ввожу два целых числа. Если они отличаются на 100, то выведите YES, иначе NO.
"""n1=int(input("Enter a number "))
n2=int(input("Enter a number "))
if n1-n2==100 or n2-n1==100:
    print("YES")
else:
    print("NO")"""
#8 апишите программу, где ввожу три целых числа. Найдите наибольшее число из них
"""n1=int(input("Enter a number "))
n2=int(input("Enter a number "))
n3=int(input("Enter a number "))
if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)"""
#9 Напишите программу, где ввожу три целых числа. Найдите наименьшее число из
"""n1=int(input("Enter a number "))
n2=int(input("Enter a number "))
n3=int(input("Enter a number "))
if n1<n2 and n1<n3:
    print(n1)
elif n2<n1 and n2<n3:
    print(n2)
else:
    print(n3)"""
#10 Напишите программу, где ввожу четыре целых числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите Not Found.
"""a=int(input("n1 "))
b=int(input("n2 "))
c=int(input("n3 "))
d=int(input("n4 "))
if a%2==0 and a>b and a>c and a>d:
    print(a)
elif b%2==0 and b>a and b>c and b>d:
    print(b)
elif c%2==0 and c>a and c>b and c>d:
    print(c)
elif d%2==0 and d>a and d>b and d>c:
    print(d)
else:
    print("Not found")"""
#11 Напишите программу, где ввожу два целых числа (месяц и год). Если такая дата существует выведите YES, иначе NO.
"""a=int(input("Enter a month number "))
b=int(input("Enter a year "))
if a>0 and a<=12 and b>=0 and b<=2021:
    print("YES")
else:
    print("NO")"""
#12 аны три натуральных числа a, b, c, записанные в отдельных строках. Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.
"""a=int(input("Define a with positive number "))
b=int(input("Define b with positive number "))
c=int(input("Define c with positive number "))
triangle=a+b>c and b+c>a and a+c>b
if triangle:
    print("YES")
else:
    print("NO")"""
#13 В компании BITLAB ACADEMY работают 3 сотрудника, которые получают заработную плату в тенге.
# Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
"""s1=int(input("zp1="))
s2=int(input("zp2="))
s3=int(input("zp3="))
if s1>=s2 and s1>=s3:
    mx=s1
elif s2>=s1 and s2>=s3:
    mx=s2
else:
    mx=s3
if s1<=s2 and s1<=s3:
    mn=s1
elif s2<=s1 and s2<=s3:
    mn=s2
else:
    mn=s3
print (mx-mn)"""
#14 апишите программу, где я ввожу три числа. Если все числа одинаковые, то выведите YES, и
"""a=int(input("n1="))
b=int(input("n2="))
c=int(input("n3="))
if a==b==c:
    print("YES")
else:
    print("NO")"""
#15 апишите программу, где я ввожу три числа. Если среди них есть одинаковые, то выведите YES, иначе NO.
"""a=int(input("n1="))
b=int(input("n2="))
c=int(input("n3="))
if a==b or a==c or b==c:
    print("YES")
else:
    print("NO")"""



