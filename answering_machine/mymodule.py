
#Можно узнать оплату, контакты тренера, расписание, рецепт супа и запросить анекдот

import  random
import time
def menu():
    text = input("Введите запрос: ").lower()

    summ = 'оплат'
    cont = 'трен'
    pl = 'расп'
    rez="суп"
    jok="анек"
    if summ in text:
        summa()
    if cont in text:
        contact()
    if pl in text:
        plan()
    if rez in text:
        rezept()
    if jok in text:
        joke()
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


def rezept ():
    print("Мясо-500г \nСвекла-300г\nТоматное пюре-2 столовые ложки")
    time.sleep(2)
    menu()

def joke ():
    a=["Учитель алгебры очень расстроился, когда нашел свою жену с двумя неизвестными.",
      " - Я по поводу объявления о продажи мёда, скажите он настоящий?\n"
       " - Липовый.",
       "-Внучок, как зовут того англичанина, с которым я дружу?\n"
        "-Паркинсон"

       ]
    randomm=random.choice(a)
    print(randomm)
    time.sleep(2)
    menu()
