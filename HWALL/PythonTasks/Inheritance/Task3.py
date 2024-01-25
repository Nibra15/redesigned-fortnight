"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject:
    def __init__(self, size):
        self.size = size

    def print_info(self):
        print(self.size)

class Star(SpaceObject):
    def __init__(self, bright):
        self.bright=bright

    def shine(self):
        print(self.bright, "звезда светит")

class Planet(SpaceObject):
    def __init__(self, human, human_year):
        self.human=human
        self.human_year=human_year

    def human2(self):
        print(self.human*self.human_year)


Moon=SpaceObject(60)
Moon.print_info()

Sirius=Star(50)
Sirius.shine()

World=Planet(200,2)
World.human2()


