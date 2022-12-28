
# * Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#   N = 6 | N = 12      | 32                | 13 | 9        | 18        | 21
#   2 * 3 | 2 * 2 * 3   | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3    | 2 * 3 * 3 | 3*7


# последнее число в списке, отнимаем единицу у него чтобы не делить на самого себя
def get_list_of_prime_factors(number):
    polynomials = [number]
    i = polynomials[len(polynomials) - 1] - 1

    while i > 1:
        last = polynomials[len(polynomials) - 1]
        if last % i == 0:
            polynomials.pop()
            polynomials.append(last // i)
            polynomials.append(i)
        i -= 1
    return polynomials


value = input('Введите целое число: ')
value = int(value)
print(get_list_of_prime_factors(value))