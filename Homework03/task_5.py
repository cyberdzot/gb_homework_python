
# * Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci_ex(count):
    list1 = []
    list2 = []
    minus = False
    old = 0
    new = 1

    for i in range(count):
        list1.append(new)
        if minus:
            list2.append(-new)
        else:
            list2.append(new)
        old, new = new, new + old
        minus = not minus

    list2.reverse()
    list2.append(0)
    return list2 + list1


value = input('Введите целое число: ')
value = int(value)

print(fibonacci_ex(value))
