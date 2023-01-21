
# * Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


my_list = [12, 'sadf', 5643]


string = filter(lambda x: not str(x).isdigit(), my_list)
digit = filter(lambda x: str(x).isdigit(), my_list)


print("Строки: ", list(string))
print("Числа: ", list(digit))
