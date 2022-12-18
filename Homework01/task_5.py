
# * Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# Результаты в примере не верны!!!

import math

def get_distance_between_two_points(x1, y1, x2, y2):
    return round(math.hypot(x2 - x1, y2 - y1), 2)


a_x = float(input('Введите x1: '))
a_y = float(input('Введите y1: '))
b_x = float(input('Введите x2: '))
b_x = float(input('Введите y2: '))

dist = get_distance_between_two_points(a_x, a_y, b_x, b_x)

print(f'Расстояние между точками A и B: {dist}')
