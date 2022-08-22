from itertools import cycle
from nim_engine import Nim_bild
from termcolor import cprint, colored

game = Nim_bild()

game.max_bunche_size, game.max_bunches, game.user_count = \
    int(input("Введите максимальное количество камней в кучке: ")), \
    int(input("Введите количество кучек: ")), \
    int(input("Введите количество игровов "))
game.settings(game.max_bunches, game.max_bunche_size, game.user_count)
user_number = cycle(game.USER_NAME.values())
user_color = "blue"
user = (next(user_number))
while True:
    cprint(f'Текущая позиция ---{game.holder}---', color='green')
    cprint(f'Ход игрока {user}  \n-откуда берем?', color=user_color)
    pos = input()
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed = game.take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_color = 'blue' if user_color == 'yellow' else 'yellow'
        user = (next(user_number))
        if 0 in game.holder:
            game.holder.remove(0)
    else:
        cprint('Невозможный ход!', color='red')
    if game.is_gameover():
        break

cprint(f'Выйграл игрок {user}', color='red')
