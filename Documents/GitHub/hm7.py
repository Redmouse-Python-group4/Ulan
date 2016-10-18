# coding: utf8

class Tovar():

    src = 'tovar.csv'

    def __init__(self):
        self.kol_pcs = 0;
        self.kol_pair = 0;

    def write_to_csv(self):
        import csv
        file = open(self.src, 'a')
        writer = csv.writer(file, delimiter = ',', quoting=csv.QUOTE_MINIMAL, quotechar='`')
        writer.writerow(['Итого штук: ', self.kol_pcs])
        writer.writerow(['Итого пар: ', self.kol_pair])

    def change_src(self):
        self.src = raw_input('Введите название файла вместе с расширением: ')

    def count(self):
        import csv
        list = csv.reader(open(self.src, 'rb'))
        for row in list:
            if str(row[2]) == 'шт':
                self.kol_pcs += int(row[1])
            elif str(row[2]) == 'пары':
                self.kol_pair += int(row[1])

odejda = Tovar()
odejda.count()
print 'Итого: %s штук' % odejda.kol_pcs
print 'Итого: %s пар'  % odejda.kol_pair
odejda.write_to_csv()
