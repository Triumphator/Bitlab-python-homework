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

#16 Напишите программу, где я ввожу три числа. Если все числа больше 10 и
# все числа делятся без остатка на 5, то выведите YES, иначе NO.
"""a=int(input("n1="))
b=int(input("n2="))
c=int(input("n3="))
fivebyfive=a>10 and b>10 and c>10 and a%5==0 and b%5==0 and c%5==0
if fivebyfive:
    print("YES")
else:
    print("NO")"""
#17 Напишите программу, где я ввожу целое число n, и если оно больше 20, поделите его на 6, иначе умножьте на 6.
# Выведите полученное число.
"""n=int(input("n="))
if n>20:
    print(n/6)
else:
    print(n*6)"""
#18 Напишите программу, где я ввожу целое число n, и если оно является положительным, то прибавьте к нему 1;
# если отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Выведите полученное число.
"""n=int(input("n="))
if n>0:
    n=n+1
elif n<0:
    n=n-2
else:
    n=10
print(n)"""
#19 Напишите программу, где я ввожу целые числа a и b, если их значения не равны, то присвоить каждой переменной сумму
# этих значении, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных.
"""a=int(input("a="))
b=int(input("b="))
if a!=b:
    a,b=a+b, a+b
else:
    a,b=0, 0
print(a,b)"""
#20 Напишите программу, где ввожу число n, и если оно является положительным, то прибавьте к нему 1; в противном случае не изменять его. Выведите полученное число.
"""n=int(input("n="))
print(n+1 if n>0 else n)"""
#21 Напишите программу, где я ввожу целостное число a и b, и если a делиться на b, то программа должна вывести divisible иначе not divisible.
#*** Подсказка: Есть такой оператор %, % показывает остаток числа.
#Например, 10%4 будет равна 2, так как когда мы делим 10 на 4, остаток у нас будет 2
"""a=int(input("a="))
b=int(input("b="))
print("divisible" if a%b==0 else "not divisible")"""
#22
"""rookH=int(input("Enter rook row position 1-8 "))
rookV=int(input("Enter rook column position 1-8 "))
row=int(input("Enter row 1-8 "))
clmn=int(input("Enter column 1-8 "))
beat=rookH==row or rookV==clmn
print("YES" if beat else "NO")"""
#23 Напишите программу, где я ввожу целое число. Если оно от 1 до 5 включительно, то увеличьте его на 10.
# Если от 10 до 20 включительно, то уменьшите его на 5. Если оно меньше 0 или более 1000, то умножаем на 3. Иначе 0.
"""n=int(input("n="))
if n>=1 and n<=5:
    n=n+10
elif n>=10 and n<=20:
    n=n-5
elif n<0 or n>1000:
    n=n*3
else:
    n=0
print(n)"""
#24 Напишите программу, где я ввожу четыре числа, если все числа больше 5, второе число делится на 4, четвертое число не делится на 3, то выведите YES, иначе NO.
"""n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))
n4=int(input("n4="))
magic=(n1,n2,n3,n4)>(5,5,5,5) and n2%4==0 and n4%3==0
print("YES" if magic else "NO")"""
#25 Напишите программу, где я ввожу два числа. Если первое число больше второго, то вывести YES, иначе поменять значения переменных и вывести.
"""a=int(input("n1="))
b=int(input("n2="))
if a>b:
    print("YES")
else:
    a,b=b,a; print(a,b)"""
#26 Напишите программу, где я ввожу номер месяца, вывести название месяца.
"""mn=int(input("Enter month number "))
if mn>=1 and mn<=12:
    Mnames=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(Mnames[mn-1])
else:
    print("Incorrect number")"""
#27 Дано натуральное число. Требуется определить, является ли год високосным. Если год является високосным, то выведите YES, иначе выведите NO.
# (Напомним, что год является високосным, если его номер делится на 4, но не делится на 100, или если он делится на 400.)
"""year=int(input("Input a year "))
leapyear=year%400==0 or (year%4==0 and year%100!=0)
print("YES" if leapyear else "NO")"""
#28 Напишите программу где я ввожу логин и пароль. И если данные были введены верно, то мы выводим Authentication completed, иначе Invalid login or password.
#(Логин должен быть user, пароль - qwerty)
"""login=input("Enter your login ")
pswd=input("Enter your password ")
if login=="user" and pswd=="qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")"""
#29 Напишите программу обмена валют, где я ввожу сумму в тенге и выбираю на какую валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8)
"""KZT=int(input("Enter amount in KZT "))
choice=int(input("Choose currency\n [1] USD\n [2] EUR\n [3] RUB\n"))
if choice>=1 and choice<=3:
    if choice==1:
        print(KZT,"KZT is",KZT/420,"USD")
    elif choice==2:
        print(KZT, "KZT is", KZT / 510, "EUR")
    else:
        print(KZT, "KZT is", KZT / 5.8, "RUB")
else:
    print("Incorrect key")"""
#30
print("Choose your branch:")
ch1=int(input("1 - Science, 2 - Humanitarian subjects, 3 - Art, 4 - Sports:\n"))
def pr(prof):
    print("You are",prof)
if ch1>=1 and ch1<=4:
    if ch1==1:
        ch2=int(input("You chose Science\n1 - Math, 2- Physics\n"))
        pr("Financier") if ch2==1 else pr("Engineer")
    elif ch1==2:
        ch2 = int(input("You chose Humanitarian subjects\n1 - History, 2- Foreign languages\n"))
        pr("Historian or Diplomat") if ch2==1 else pr("Translator")
    elif ch1==3:
        ch2 = int(input("You chose Art\n1 - Drawing, 2 - Singing\n"))
        pr("Painter or Architect") if ch2 == 1 else pr("Singer or Tamada")
    else:
        ch2 = int(input("You chose Sports\n1 - Team, 2 - Individual\n"))
        pr("Football or Basketball player") if ch2 == 1 else pr("Boxer or Tennis player")
else:
    print("Incorrect number")



