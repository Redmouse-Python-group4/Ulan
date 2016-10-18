# -*- coding: utf-8 -*-

from pack import hw1.2
 
print u"Общество в начале XXI века"
age=int(raw_input("Введите ваш возраст "))
if 0<=age<=7:
    print hw1.2.func1_7(age)
elif age<=18:
    print hw1.2.func7_18(age)
elif age<=25:
    print hw1.2.func18_25(age)
elif age<=60:
    print hw1.2.func25_60(age)
elif age<=120:
    print hw1.2.func60_120(age)
else:
    print hw1.2.error()
