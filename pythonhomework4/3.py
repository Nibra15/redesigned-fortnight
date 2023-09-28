price_one =int(input())
price_two =int(input())
price_three =int(input())

if price_one < price_two and price_two < price_three:
    print("Акция!", round((price_one + price_two + price_three) / 2, 2))
elif price_one > price_two and price_two > price_three:
    print("Акция!", round((price_one+price_two+price_three)/3,2))
else:
    print(price_one+price_two+price_three)

