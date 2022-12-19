
# * Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_factorial(num):
    list = []
    product = 1
    for i in range(1, num+1):
        product *= i
        # list.append( value ) - добавляет значение в конец списка.
        list.append(product)
    return list


number = int(input('Введите число(от 1): '))
print(get_factorial(number))
