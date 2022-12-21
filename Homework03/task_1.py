
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_number = []


def get_sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


count = int(input('Сколько чисел вводим: '))

for i in range(1, count+1):
    list_number.append(int(input(f'Число №{i}: ')))

print(f'Наш список: {list_number}')
print(f'Наша сумма: {get_sum(list_number)}')
