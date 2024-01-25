"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import datetime
class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def print_info(self):
        print(self.name, self.age)

    @classmethod
    def new_person(cls,year):
        return Person("Oleg",datetime.today().year-year)


    @staticmethod
    def check_age(age):
        if age>18:
            print("Вам 18")
        else:
            print("Вход в бар запрещен")

Oleg=Person("Oleg", 21)
Oleg.print_info()
New_Oleg=Oleg.new_person(1998)
New_Oleg.print_info()
New_Oleg.check_age(16)