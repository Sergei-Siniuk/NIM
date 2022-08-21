from random import randint

USER_NAME = {}
holder = []

def settings(max_bunches, max_bunche_size, count_plaer):
    for i in range(int(count_plaer)):
        USER_NAME[i] = input(f"Введите имя {i + 1} игрока:")

    def put_stones():
        """ расположить камни на игровой поверхности """
        for i in range(1, max_bunches + 1):
            holder.append(randint(1, max_bunche_size))
    return put_stones()


def take_from_bunch(position, quantity):
    if holder[position - 1] - quantity >= 0:
        holder[position - 1] -= quantity
        return True
    else:
        return False


def is_gameover():
    return sum(holder) == 0
