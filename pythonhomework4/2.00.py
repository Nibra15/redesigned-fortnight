price = int(input("Введите стоимость:"))
time = int(input("Введите время"))

if time  > 10 and time <  12:
    print(price/2)
elif time > 20 and time < 22:
    print(price/4)
else:
    print(price)
