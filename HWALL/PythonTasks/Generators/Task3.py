"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
generate = (i for i in range(100) if i % 11 == 0)
for i in generate:
    print(i)