
# * Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# * Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3, 4]


list_index = [2, 1, 0, 5, 6]
list_number = []

# наполним от -N до N
def list_fill(num):
    for i in range(-num, num+1):
        list_number.append(i)


# вставим 2 списка и узнаем произведение
def product_index(index, number):
    temp = number[index[0]]
    for i in index[1:]:
        temp *= number[i]
    return temp


number = int(input('Введите N: '))
list_fill(number)

print(list_number)
print(f'Произведение равно: {product_index(list_index, list_number)}')
