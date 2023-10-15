"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""

def function (*numbers):
    average=sum(numbers)/len(numbers)
    chislo=[]

    for i in  numbers:
        if i >average:
            chislo.append(i)

    print(average,chislo)

function(20,40,5)














