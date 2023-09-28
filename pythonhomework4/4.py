tovar = input().lower()
if tovar ==  "продукты":
    price= int(input("Введите цену"))
    if price <100:
        print("Выпечка")
    elif price >100 and  price < 500:
        print("Орехи")
    else:
        print("Фрукты")
else:
    print("Загляните в товары для дома")