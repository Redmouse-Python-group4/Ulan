# -*- coding: utf-8 -*-

def func1_3(x):
	result = ''
	str=raw_input("Введите строку ")
	n=int(raw_input("Введите число повтров "))
	for i in range(0, n):
		result += str + '\n'
	return result

def func4_6(x):
	m=int(raw_input("Введите степень "))
	return "%s в степени %s равно %s"%(x, m, x**m)

def func7_9(x):
	result = ""
	for i in range(0, 10):
		x+=1
		result+="%s \n" % x
	return result
