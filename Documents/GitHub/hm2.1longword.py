st=input('Введите строку: ').split()
count=0
for i in st:
    if len(i)>count:
        count=len(i)
        word=i    
print('Самое длинное слово: ',word)
