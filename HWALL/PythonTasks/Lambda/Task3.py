"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
name = input("Введите имя: ")

new_name = (lambda name: name + " Гений") if name[-1] in ['А', 'Я', 'Г', 'М'] else (lambda name: name + " Сверхразум") if name[-1] in ['О', 'Ь', 'Л', 'Н'] else (lambda name: "Просто " + name)

x = new_name(name)
print (x)

