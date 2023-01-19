
# * Создайте программу для игры в ""Крестики-нолики"" человек vs человек.


EMPTY = ' '

gamer = "X"
field_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field_value = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]


def game_show(field, message='Игра начинается!'):
    # спрячем мусор в терминале :)
    print("\033[H\033[J")

    print('\n')
    print(message)
    print('\n')
    print(f'\t{field_id[0]}    |  {field_id[1]}  |    {field_id[2]}')
    print(f'\t  {field[0]}  |  {field[1]}  |  {field[2]}')
    print('\t_____|_____|_____')
    print(f'\t{field_id[3]}    |  {field_id[4]}  |    {field_id[5]}')
    print(f'\t  {field[3]}  |  {field[4]}  |  {field[5]}')
    print('\t_____|_____|_____')
    print(f'\t{field_id[6]}    |  {field_id[7]}  |    {field_id[8]}')
    print(f'\t  {field[6]}  |  {field[7]}  |  {field[8]}')
    print('\t     |     |')
    print('\n')


def game_update(number, option):
    global field_value
    global field_id

    field_value[number - 1] = option
    field_id[number - 1] = EMPTY


def get_field_value(cell, _id):
    return cell[_id - 1]


def change_player():
    global gamer

    if gamer == "X":
        gamer = "O"
    else:
        gamer = "X"


def play():
    global gamer
    global field_value

    game_show(field_value)

    while field_value.count(EMPTY) != 0:
        number = input()
        number = int(number)

        if number == 0:
            # выход из игры досрочно!
            fstr = f'Игрок "{gamer}" сдался, игра окончена!'
            game_show(field_value, fstr)
            return
        elif 0 < number < 10:
            if get_field_value(field_value, number) != EMPTY:
                fstr = f'Ход игрока "{gamer}"! Подсказка: выбранная ячейка уже занята, выберите другую.'
                game_show(field_value, fstr)
            else:
                game_update(number, gamer)
                change_player()
                fstr = f'Ход игрока "{gamer}"! Подсказка: чтобы покинуть игру введите цифру: 0.'
                game_show(field_value, fstr)
        else:
            fstr = f'Ход игрока "{gamer}"! Введена не существующая ячейка!'
            game_show(field_value, fstr)

    # ! тут результаты надо посчитать и прописать победа чья то или ничья
    # gamer = get_winner()
    # fstr = f'Победил игрок "{gamer}"! Игра окончена!'
    # game_show(field_value, fstr)


# ! дописать надо будет
# def get_winner():
#     global gamer
#     global field_value

#     options = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
#     for element in field_value:
#         print(element)
#     return


play()