"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def IMT(weight,height):
    x=(weight/height*height)
    return x

def wes (IMT):
    if IMT<18.5:
        print("Недостаточный вес")
    elif IMT>18.5 and IMT < 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

x=int(input())
y=int(input())


imt=IMT(x,y)
wes(imt)