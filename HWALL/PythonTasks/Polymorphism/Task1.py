"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class human:

    def _print(self):
        print("Имитирую кряканье")


    def clothes(self):
        print("wear clothes")


class duck:

    def _print(self):
        print("Кряканье")

    def clothes(self):
        print("wear clothes")

duck_1=duck()
human_1=human()

for a in (duck_1,human_1):
    a._print()
    a.clothes()



