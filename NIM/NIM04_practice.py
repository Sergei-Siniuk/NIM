from itertools import cycle
from nim_engine import holder, is_gameover, take_from_bunch, settings, USER_NAME
from termcolor import cprint, colored

max_bunche_size, max_bunches, user_count = \
    int(input("Введите максимальное количество камней в кучке: ")), \
    int(input("Введите количество кучек: ")), \
    int(input("Введите количество игровов "))
settings(max_bunches, max_bunche_size, user_count)

user_number = cycle(USER_NAME.values())
user_color = "blue"
user = (next(user_number))
while True:
    cprint(f'Текущая позиция ---{holder}---', color='green')
    cprint(f'Ход игрока {user}  \n-откуда берем?', color=user_color)
    pos = input()
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_color = 'blue' if user_color == 'yellow' else 'yellow'
        user = (next(user_number))
        if 0 in holder:
            holder.remove(0)
    else:
        cprint('Невозможный ход!', color='red')
    if is_gameover():
        break

cprint(f'Выйграл игрок {user}', color='red')
