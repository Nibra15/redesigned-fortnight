"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def function (name=None,age=None,salary=None):
    if name != None  and age != None and salary != None:
        print(name,age,salary)
    else:
        print(None)



function()