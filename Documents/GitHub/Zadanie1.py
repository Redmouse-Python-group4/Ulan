x = int(input ("Введите число от 1 до 9:"))
if x>=1 and x<=3:
    s = str(input("Введите строку:"))
    n = int(input("Введите кол-во повторов строки:"))
    i = 0
    while i <n:
        print (s)
        i =i+1

elif x>=4 and x <=6:
    m = int(input("Введите степень, в котору, следует возвести число:"))
    print (x**m)
elif x >= 7 and x <=9:
    i = 0
    while i <10:
        x = x+1
        i = I+1
        print (x)
else:
    print("Ошибка ввода")

    #Пробный комментарий, чтобы проверить сохраняется ли программа в Github
