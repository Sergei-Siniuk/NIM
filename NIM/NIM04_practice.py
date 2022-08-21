from nim_engine import put_stones, holder, is_gameover, take_from_bunch,settings,USER_NAME,gena
from termcolor import cprint, colored
max_bunche_size,max_bunches,user_count=int(input("Введите максимальное количество камней в кучке: ")),\
                                       int(input("Введите количество кучек: ")),\
                                       int(input("Введите количество игровов "))
settings(max_bunches,max_bunche_size,user_count)
put_stones()
user_number = gena(USER_NAME)
user_color="blue"
user=(next(user_number))
while True:
    cprint(f'Текущая позиция \n {holder}', color='green')
    cprint('Ход игрока {}'.format(user), color=user_color)
    pos = input(colored('Откуда берем?', color=user_color))
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

cprint('Выйграл игрок номер {}'.format(user), color='red')
