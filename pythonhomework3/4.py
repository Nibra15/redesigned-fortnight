category = input("введите категорию")
price = 0
if  category == "продукты":
    price = int(input("введите цену"))
    if price <= 100:
        print(" попробуйте нашу выпечку!")
    if price >= 100 and price<= 500:
        print("как на счёт орехов в шоколаде?")
    if price >= 500:
        print("попробуйте экзотические фрукты!")
else:
    print ("Загляните в товары для дома!")


