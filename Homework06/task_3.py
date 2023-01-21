
# * Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def get_sum(number):
    digit = filter(lambda x: x.isdigit(), str(number))
    return sum(map(int, list(digit)))


number = input("Введите вещественное число: ")

print(f"Сумма цифр в числе: {get_sum(number)}")
