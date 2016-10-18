# -*- coding: utf-8 -*-

class HW1_2():
	
	def __init__(self, age):
		print u"Общество в начале XXI века"
		self.age = age
		if 0<=self.age<=7:
		    print self.func1_7()
		elif self.age<=18:
		    print self.func7_18()
		elif self.age<=25:
		    print self.func18_25()
		elif self.age<=60:
		    print self.func25_60()
		elif self.age<=120:
		    print self.func60_120()
		else:
		    print self.error()

	def func1_7(self):
	    return u"Вам в детский сад"

	def func7_18(self):
	    return u"Вам в школу"

	def func18_25(self):
	    return u"Вам в профессиональное учебное заведение"

	def func25_60(self):
	    return u"Вам на работу"
	
	def func60_120(self):
	    return u"Вам предоставляется выбор"

	def error(self):
	    error = u"Ошибка! Это программа для людей!\n"
	    return error*5
