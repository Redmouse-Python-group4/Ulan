# -*- coding: utf-8 -*-
 
import time
from datetime import datetime, timedelta, date

print '-'*50
print("Problem#1")
print '-'*50
x = 20160305
print(datetime.strptime(str(x), '%Y%m%d'))

print '-'*50
print("Problem#2")
print '-'*50
day = 25
month = 2
year = 2016
print(datetime.strptime(str(day)+str(month)+str(year), '%d%m%Y'))

print '-'*50
print('Problem#3')
print '-'*50
st = '01/05/2016'
print(datetime.strptime(st, '%d/%m/%Y'))

print '-'*50
print('Problem#4')
print '-'*50
today = datetime.today()
print(today)
a = today.replace(year=(today.year+1), month=(today.month-1))
print(a)
print(a.strftime('%j'))
print(a.timetuple().tm_yday)

print '-'*50
print('Problem#5')
print '-'*50
n = 25
print datetime(datetime.today().timetuple().tm_year, 1, 1) + timedelta(n - 1)

print '-'*50
print('Problem#6')
print '-'*50
d = date.today()
print d.strftime('%j')

print '-'*50
print('Problem#7')
print '-'*50
dt = str(raw_input('Input a date in dd.mm.yyyy format: '))
dd = datetime.date(datetime.strptime(dt, '%d.%m.%Y'))
dm = time.strftime('%B %d %y', dd.timetuple())
print dm
