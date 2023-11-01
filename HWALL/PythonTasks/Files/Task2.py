"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

text= "но у меня не получается"
with open ("example2.txt", "w") as file:
    file.write(text)
with open ("test.txt", "r")as file:
    s = file.read()
with open ("example2.txt", "r")as file:
    b = file.read()
with open ("example2.txt", "w")as file:
    file.write(s+ " "+b)





