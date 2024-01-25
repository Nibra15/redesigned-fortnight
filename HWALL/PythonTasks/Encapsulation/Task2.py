"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
import time
class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.weapon = weapon

    def print_info(self):
        print(f"Появился герой: {self.name}, держащих в руках оружие: {self.weapon}")

    def strike(self, enemy):
        print(f"{self.name} ударяет {enemy.name}")
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(f"У героя {self.name} осталось {self.health} здоровья и {self.armor} брони")

    def fight(self, enemy):
        print(f"Начался бой между {self.name} и {enemy.name}")
        while True:
            self.strike(enemy)
            time.sleep(1)
            enemy.strike(self)
            time.sleep(1)
            if self.health <= 0:
                print(f"{self.name} погиб")
                break
            elif enemy.health <= 0:
                print(f"{enemy.name} погиб")
                break

    def regeneration(self, enemy):
        self.health += 20
        enemy.health += 20

    def stay_alive(self, enemy):
        if self.health <= 0:
            print(f"Вы оживили {self.name}!")
            self.health = 20
        if enemy.health <= 0:
            print(f"Вы оживили {enemy.name}")
            enemy.health = 20


artur = Hero("artur", 100, 30, 20, "меч")
solovey = Hero("solovey", 100, 20, 30, "лук")
artur.fight(solovey)
