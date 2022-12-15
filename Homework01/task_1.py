#################
# ! тест1
# ? тест2
# * тест3
# TODO тест4
#################

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

IS_DAYS = [False, False, False, False, False, True, True]

def is_day_off(arg):
    if 0 < arg < 8:
        return IS_DAYS[arg - 1]
    return


day = int(input('Введите день недели: '))

status = is_day_off(day)

if status == None:
    print('Такого дня недели не существует!')
elif status:
    print('Этот день является выходным.')
else:
    print('Этот день является рабочим.')