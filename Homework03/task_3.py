
# * Задайте список из вещественных чисел.
# * Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ? Из примера я так понимаю нужно учесть, что 0 не является минимальным значением...

list_number = []


def get_difference_between_max_and_min(list):

    min = round(list[0] - int(list[0]), 2)
    max = min

    for i in list:
        i = round(i - int(i), 2)
        if i < min:
            min = i
        if i > max:
            max = i

    return round(max - min, 2)


count = int(input('Сколько вещественных чисел вводим: '))

for i in range(1, count+1):
    list_number.append(float(input(f'Веществ. число №{i}: ')))

result = get_difference_between_max_and_min(list_number)
print(f'Разница: {result}')
