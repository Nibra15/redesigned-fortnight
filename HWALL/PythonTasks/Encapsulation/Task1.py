"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class BankAccount:
    def __init__(self, name, password, balance, passport):
        self.name=name
        self._password=password
        self.__balance=balance
        self.__passport=passport
    def get_balance(self,pin):
        if pin == self._password:
            return self.__balance
        return "Пароль не подходит"


    def get_passport(self,pin):
        if pin == self._password:
            return self.__passport
        return "Пароль не подходит"

    def set_balance(self,amount):
        if self.__balance - amount <0:
            return "денег нет"
        self.__balance -= amount
        return "вы сняли деньги"

    def del_pass (self,pin):
        if pin == self._password:
            return "Вы удалили паспорт"
        return "Пароль не верный"

Oleg=BankAccount("Oleg", 1234, 10000,2145)
print(Oleg.get_balance(1234))
print(Oleg.get_passport(1234))
print(Oleg.set_balance(50))
print(Oleg.del_pass(1234))
