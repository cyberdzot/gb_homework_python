
# * Задайте последовательность чисел.
# * Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


def get_elements_without_repet(arg_list):
    func_list = []

    for e in arg_list:
        if arg_list.count(e) == 1:
            func_list.append(e)

    return func_list


my_list = [3, 1, 2, 3, 4, 2]

print(get_elements_without_repet(my_list))