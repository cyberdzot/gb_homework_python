
# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

def get_smallest_divisor(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i


number = int(input('Введите целое число(от 2): '))

print(f'Ответ: {get_smallest_divisor(number)}')
