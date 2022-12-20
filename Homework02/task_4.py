
# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

def get_summ(num):
    sum = 0
    for i in range(2, num+1, 2):
        sum += i
    return sum

number = int(input('Введите число(от 2):'))
print(f'Сумма чётных чисел: {get_summ(number)}')
