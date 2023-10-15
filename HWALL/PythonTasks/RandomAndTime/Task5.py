"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""

import random
import time


kub_1=0
kub_2=0
kub_1= random.randint(1,6)
kub_2= random.randint(1,6)
time.sleep(5)
print(kub_1,kub_2)


