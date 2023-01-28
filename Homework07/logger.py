
# * логирование


from datetime import datetime

PATH_FOR_LOG = 'log.csv'

FORMAT_DATETIME = '%H:%M:%S'
# %m/%d/%Y, %H:%M:%S



def add_action_log(name, desc):
    time = datetime.now().strftime(FORMAT_DATETIME)
    with open(PATH_FOR_LOG, 'a') as file:
        file.write(f'{time};{name};{desc}\n')







# отладка
if __name__ == "__main__":
    add_action_log('test', 'data_test')