# -*- coding: utf-8 -*-

def str_split(mystr):
	result=""
	for word in mystr.split():
		result+="%s - %s \n"%(word, len(word))
	return result

print str_split(raw_input("Введите строку "))

def cs(*arg):
	mypow=1
	result = list()
	for i in arg:
		result.append(i**cs)
		cs=i
	return result

print cs(2, 11, 12, 12, 4, 6)
