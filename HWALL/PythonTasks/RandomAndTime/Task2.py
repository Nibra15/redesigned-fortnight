"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""

from random import  randint
sport1=2
sport2=0
amout1= int(input("Введите кол/во спортсемнов"))
print("Число участников сборной:",amout1)
amout2= int(input("Введите кол/во спортсемнов"))
print("Число участников сборной:",amout2)


while sport1 != sport2:
    sport1 = randint(1,amout1)
    sport2=randint(1,amout2)
    print("Пловец-", sport1, "-" ,"Пловец-",sport2)