
#* Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


value = int(input('Введите целое число: '))

print(f'Двоичный формат: {convert_to_binary(value)}')
