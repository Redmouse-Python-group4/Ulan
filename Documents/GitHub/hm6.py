#coding=utf-8
from abc import ABCMeta, abstractmethod, abstractproperty

class Unknown():
    __metaclass__ = ABCMeta
    x = 0

class Task1(Unknown):    # HomeWork 1.1

    def __init__(self):
        self.x = self.get_integer('Введите число от 1 до 9: ')
        if  (self.x < 1 or self.x > 9):
            print "Введенная цифра меньше 1 или больше 9 !"
        elif self.x <= 3:    # Option 1
            print self.option_1()
        elif self.x <= 6:    # Option 2
            print self.option_2()
        elif self.x <= 9:    # Option 3
            print self.option_3()


    def get_integer(self, text):
        """Function returns integer until it is True"""
        y = False
        while not y:
            try:
                input_value = int(raw_input(text))
            except ValueError:
                print 'Это не цифра !'
            else:
                y = True
                return int(input_value)

    def option_1(self):
        return raw_input('Введите строку: ') * self.get_integer('Введите цифру: ')

    def option_2(self):
        return self.x ** self.get_integer('Введите степень: ')

    def option_3(self):
        return  [self.x for self.x in range(self.x+1,self.x+11)]

class Child(Task1):
    def __init__(self):
        super(Child, self).__init__()

a = Child()
