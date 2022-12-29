
# * Задана натуральная степень k.
# * Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом

# "значения от 0" - с нулями выражений я не видел, могу ошибаться, поэтому буду делать от 1 до 100


import random as rand


def get_polynomial(pow):
    string = ''

    for i in range(pow, 1, -1):
        string += str(rand.randint(1, 99)) + 'x^' + str(i) + ' + '

    return string + str(rand.randint(1, 99)) + 'x + ' + str(rand.randint(1, 99))


k = input('Введите степень: ')
k = int(k)
print(get_polynomial(k))
