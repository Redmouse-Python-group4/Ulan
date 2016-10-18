# -*- coding: utf-8 -*-
class HW1_1():
	
	def __init__(self, x):
		self.x = x
		if 0<=self.x<=3:	
			print self.func1_3()
		elif 4<=self.x<=6:
			print self.func4_6()
		elif 7<=self.x<=9:
			print self.func7_9()
		else:
		    print u"Ошибка ввода!\n"
	
	def func1_3(self):
		result = ''
		str=raw_input("Введите строку ")
		n=int(raw_input("Введите число повтров "))
		for i in range(0, n):
			result += str + '\n'
		return result

	def func4_6(self):
		m=int(raw_input("Введите степень "))
		return "%s в степени %s равно %s"%(self.x, m, self.x**m)

	def func7_9(self):
		result = ""
		x = self.x
		for i in range(0, 10):
			x+=1
			result+="%s \n" % x
		return result
