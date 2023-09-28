product_one = int(input())
product_two = int(input())
product_three = int(input())
sum=(product_one+product_two+product_three)
if product_one == 25 and product_two == 100 and product_three == 310:
    print("Акция!", sum//2)
elif product_one == 2500 and product_two == 400 and product_three == 50:
    print("Акция!", sum // 3)
else:
    print("к оплате", sum)