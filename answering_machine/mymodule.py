

import time
def menu():
    text = input("Введите запрос: ").lower()

    summ = 'оплат'
    cont = 'трен'
    pl = 'расп'
    adr= 'адрес'
    prot='прот'

    if summ in text:
        summa()
    if cont in text:
        contact()
    if pl in text:
        plan()
    if adr in text:
        adres()
    if prot in text:
        protein()
    else:
        menu()


def contact():
    print("Контактный телефон тренера:+794814814814")
    time.sleep(2)

    menu()


def summa():
    print("К оплате 500 рублей")
    time.sleep(2)

    menu()


def plan():
    print("Рассписание: в четверг 19 часов")
    time.sleep(2)
    menu()

def adres():
    print("Олимпийский просп. 1")
    time.sleep(2)
    menu()

def protein():
    print("2-3г протеина на 1 кг веса")
    time.sleep(2)
    menu()
