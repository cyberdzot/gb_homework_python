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

is_days = [False, False, False, False, False, True, True]

def IsDayOff(arg):
    if 0 < arg < 8:
        return is_days[arg - 1]
    return


day = int(input('Введите день недели: '))

status = IsDayOff(day)

if status == None:
    print('Такого дня недели не существует!')
elif status:
    print('Этот день является выходным.')
else:
    print('Этот день является рабочим.')