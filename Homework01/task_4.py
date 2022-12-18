
# * Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 2|1
# 3|4

QUARTER_TEXT = [
    'Диапазон координат в 1 четверти:\nX: (0, +∞)\nY: (0, +∞)',
    'Диапазон координат во 2 четверти:\nX: (-∞, 0)\nY: (0, +∞)',
    'Диапазон координат в 3 четверти:\nX: (-∞, 0)\nY: (-∞, 0)',
    'Диапазон координат в 4 четверти:\nX: (0, +∞)\nY: (-∞, 0)',
    'Четверть не существует!'
]

def find_range_coordinates(quarter):
    if quarter == 1:
        return 0
    elif quarter == 2:
        return 1
    elif quarter == 3:
        return 2
    elif quarter == 4:
        return 3
    else:
        return 4


i_quarter = int(input('Введите номер четверти [1-4]: '))
result = find_range_coordinates(i_quarter)

print(QUARTER_TEXT[result])