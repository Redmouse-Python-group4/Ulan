# coding: utf8

from abc import ABCMeta, abstractmethod, abstractproperty

class Unknown():
    __metaclass__ = ABCMeta
    x = 0

class Task2(Unknown):  # HomeWork 1.2
    list = ('Ошибка это программа для людей', 'Вам в детский сад !', 'Вам в школу',
            'Вам в профессиональное учебное заведение', 'Вам на работу', 'Вам предоставляется выбор')

    def __init__(self):
        print u'Общество в начале XXI века\n'
        self.x = self.get_integer('Введите ваш возраст: ')
        if (self.x <= 0 or self.x > 120):
            print self.list[0]
        elif self.x <= 6:    # Option 1
            print self.list[1]
        elif self.x <= 17:   # Option 2
            print self.list[2]
        elif self.x <= 24:   # Option 3
            print b.list[3]
        elif self.x <= 59:   # Option 4
            print self.list[4]
        elif self.x <= 120:  # Option 5
            print self.list[5]

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

class Child(Task2):
    def __init__(self):
        super(Child, self).__init__()

b = Child()
