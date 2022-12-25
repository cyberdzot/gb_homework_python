
# * Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]


def get_product(list):
    result = []
    l_len = len(list)
    hf_len = l_len / 2

    if hf_len % 2 != 0:
        hf_len = int(hf_len + 1)

    # for i, e in enumerate(list):
    for i in range(l_len):
        if i < hf_len:
            result.append(list[i] * list[l_len-1-i])

    return result


print(get_product(list2))
