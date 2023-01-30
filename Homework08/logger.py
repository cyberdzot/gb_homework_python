
# * логирование


from datetime import datetime

PATH_FOR_LOG    = 'log.csv'
FORMAT_DATETIME = '%H:%M:%S'
one_print       = False


def add_action_log(name, desc):
    time = datetime.now().strftime(FORMAT_DATETIME)
    with open(PATH_FOR_LOG, 'a') as file:
        file.write(f'{time};{name};{desc}\n')


def new_print(*args):
    global one_print
    if not one_print:
        one_print = True
        print("\033[H\033[J")
    print(*args)

# отладка
if __name__ == "__main__":
    print("\033[H\033[J")
    add_action_log('test', 'data_test')
