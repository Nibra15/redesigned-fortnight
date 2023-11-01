"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
example="asdfghjklöwertzuio1234567890"
gen_obj=(i for i in example if i not in "1234567890")

for i in gen_obj:
    print(i)
