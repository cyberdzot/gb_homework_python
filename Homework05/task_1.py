
# * Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход делает человек.
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99
# бот 4 -> 95 ....
# бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота
# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

import random as rand


def game_candy(max_candy, max_take_candy):

    while max_candy != 0:
        player_count = input()
        player_count = int(player_count)

        if 0 < player_count < max_take_candy + 1:
            max_candy -= player_count
            if max_candy > 0:
                print(f'Вы взяли {player_count} конфет(ы).')
            else:
                print(f'Вы взяли {player_count + max_candy} конфет(ы).')
                print(f'Игра окончена! Вы победили!')
                max_candy = 0
                break

            bot_count = rand.randint(1, max_take_candy + 1)
            max_candy -= bot_count
            if max_candy > 0:
                print(f'Бот взял {bot_count} конфет(ы).')
            else:
                print(f'Бот взял {bot_count + max_candy} конфет(ы).')
                print(f'Игра окончена! Бот победил!')
                max_candy = 0
                break
        else:
            print('Вы взяли неверное количество конфет! Возьмите ещё раз, можно от 1 до 29!')


# спрячем мусор в терминале :)
print("\033[H\033[J")

game_candy(120, 28)
