from random import randint


class Nim_bild:
    def __init__(self):
        self.USER_NAME = {}
        self.holder = []
        self.max_bunches = 0
        self.max_bunche_size = 0

    def settings(self, max_bunches, max_bunche_size, count_plaer):
        for i in range(int(count_plaer)):
            self.USER_NAME[i] = input(f"Введите имя {i + 1} игрока:")
            self.put_stones()

    def put_stones(self):
        """ расположить камни на игровой поверхности """
        for i in range(1, self.max_bunches + 1):
            self.holder.append(randint(1, self.max_bunche_size))

    def take_from_bunch(self, position, quantity):
        if self.holder[position - 1] - quantity >= 0:
            self.holder[position - 1] -= quantity
            return True
        else:
            return False

    def is_gameover(self):
        return sum(self.holder) == 0
