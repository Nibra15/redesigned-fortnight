"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""
with open("example3.txt", "r", encoding='utf-8') as f:
    text=f.readlines()
    dictt = dict()
    for strings in text:
        string = strings.split()
        for sym in string:
            if dictt.get(sym) is not None:
                dictt[sym] += 1
            else:
                dictt[sym] = 1
    dictt = sorted(list(list(dictt.items())), key=lambda x: x[1], reverse=True)
    print(list(dictt)[0][0])

