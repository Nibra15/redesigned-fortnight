a = 0
while True:
    inp = input("Напишите game").lower()
    if inp == "game":
        for i in range(3):
            a = int(input())
            if a == 5:
                print("Вы Выиграли")
                break
            else:
                print("")

    elif inp == "off":
        break
