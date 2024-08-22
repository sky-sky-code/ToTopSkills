class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')


x = Gizmo()


# y = Gizmo() * 10


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick("Charli")
bus1.drop('Alice')
bus2 = HauntedBus()
bus2.pick('Nill')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)

"""
Защитное программирование при наличии изменяемых
параметров
"""

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']


class TwilightBus:
    """Автобус, из которого бесследно исчезают пассажиры"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus = TwilightBus(basketball_team)
bus.drop('Sue')
bus.drop('Maya')
print(basketball_team)
"""
чтобы сохранить собственный список пассажиров надо 
в init TwinlightBus создать копию списка или преобразовать через list:

def __init__(self, passengers=None):
     if passengers is None:
        self.passengers = []
     else:
        self.passengers = list(passengers)
"""
#######################################################################################################################
"""
DEL и сборка мусора

del - удаляет ссылки на объект, а не сам объект. 
Объект удаляется сборщиком мусора, если на него перестают указывать ссылки
"""



