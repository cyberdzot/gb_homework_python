
# * Пользователь вводит число.
# * Вам необходимо вывести число Пи с той точностью знаков после запятой,
# * сколько указал пользователь(БЕЗ round())


from math import pi


def pi_round(count):
    if count < 1:
        return 3
    else:
        return float(str(pi)[:2+count])


count = input('Введите целое число: ')
count = int(count)
print(pi_round(count))