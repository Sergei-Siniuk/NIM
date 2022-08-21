from itertools import cycle
from random import randint

USER_NAME = {}
holder = []



def settings(max_bunches, max_bunche_size, count_plaer):
    for i in range(int(count_plaer)):
        USER_NAME[i] = input(f"Введите имя {i + 1} игрока:")

    global MAX_BUNCHES, MAX_BUNCHE_SIZE
    MAX_BUNCHES = max_bunches
    MAX_BUNCHE_SIZE = max_bunche_size

def put_stones():
    """ расположить камни на игровой поверхности """
    for i in range(1, MAX_BUNCHES + 1):
        holder.append(randint(1, MAX_BUNCHE_SIZE))



def gena(a):
    c = cycle(a.values())

    def generate(c):
        for i in c:
            yield i

    return generate(c)






def take_from_bunch(position, quantity):
    if holder[position - 1] - quantity >= 0:
        holder[position - 1] -= quantity
        return True
    else:
        return False


def is_gameover():
    return sum(holder) == 0
