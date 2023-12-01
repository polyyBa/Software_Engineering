# Создаем класс Tomato
class Tomato:
    # Создаем статическое свойство states
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    # Создаем метод init
    def __init__(self, index):
        # Динамическое свойство _index
        self._index = index
        # Динамическое свойство _state
        self._state = self.states['Отсутствует']  # Изначальное состояние - зеленый

    # Создаем метод grow
    def grow(self):
        if self._state == self.states['Красный']:  # Если томат красный - не переводим
            pass
        elif self._state == self.states['Зеленый']:
            self._state = self.states['Красный']
        elif self._state == self.states['Цветение']:
            self._state = self.states['Зеленый']
        else:
            self._state = self.states['Цветение']

    # Создаем метод is_ripe
    def is_ripe(self):
        return self._state == self.states['Красный']


# Создаем класс TomatoBush
class TomatoBush:

    # Определяем метод init
    def __init__(self, num):
        # Динамическое свойство tomatoes
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    # Создаем метод grow_all
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Создаем метод all_are_ripe
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    # Создаем метод give_away_all
    def give_away_all(self):
        self.tomatoes = []


# Создаем класс Gardener
class Gardener:
    def __init__(self, name, plant):
        # Публичное войство name
        self.name = name
        # Динамическое свойство _plant
        self._plant = plant

    # Создаем метод work
    def work(self):
        self._plant.grow_all()

    # Создаем метод harvest
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран.")
        else:
            print("Плоды еще не дозрели.")

    # Создаем статический метод knowledge_base
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ")
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Удаляйте поврежденные листья и плоды, чтобы предотвратить распространение болезней')


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создаем объекты классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener('Иван', bush)

# Ухаживаем за помидорами
gardener.work()
gardener.work()
gardener.harvest()  # Плоды еще не дозрели

# Продолжаем ухаживать за помидорами
gardener.work()
gardener.work()
gardener.harvest()  # Урожай собран