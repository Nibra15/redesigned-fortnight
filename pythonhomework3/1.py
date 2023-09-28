pay = int(input("введите сумму"))
hours = int(input("введите время"))
if hours == 10  or hours == 11 or hours == 12 :
    print(pay/2)
elif hours == 20  or hours == 21 or hours == 22 :
    print(pay/4)
else:
    print(pay)