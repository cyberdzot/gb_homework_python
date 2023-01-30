
# * работа с базой данных

from logger import new_print as print
from os.path import isfile



def base_init(name):
    f = open(name + '.txt', "a")
    f.close()


# импорт успеваемости c возможной перезаписью
def import_performance(data, name):
    with open(name + '.txt', 'w') as f:
        i = -1
        for count_line in data:
            i += 1
            for subject in count_line.keys():
                fstr = subject + ':'
                count = 0
                for grades in data[i][subject]:
                    fstr += grades + ','
                    count += 1
                    if len(data[i][subject]) == count:
                        f.write(fstr + '\n')


# экспорт всей успеваемости     'surname.txt' => [ { 'subject': ['2', '3', '4', '5'] } ]
def export_performance(name):
    data = []
    base_init(name)
    with open(name + '.txt', "r") as f:
        i = -1
        for line in f:
            # считаем строки для создания списка
            i += 1
            # уберём перенос строки
            line = line.replace('\n', '')
            # разделяем предмет и оценки
            line = line.split(':')

            subject = line[0]
            grades = line[1].split(',')

            data.append({})
            data[i][subject] = grades[:-1]
    return data


# внесение правок по успеваемости
def edit_performance(data, sub, gra):
    i = -1
    for count_line in data:
        i += 1
        for subject in count_line.keys():
            if sub == subject:
                data[i][sub].append(gra)
                return data

    i += 1
    data.append({})
    data[i][sub] = []
    data[i][sub].append(gra)

    return data


def write(nam, sub, gra):
    data = export_performance(nam)
    data = edit_performance(data, sub, gra)
    import_performance(data, nam)


def read(nam, sub):
    grades = []
    if not isfile(nam + '.txt'):
        return grades
    with open(nam + '.txt', "r") as f:
        i = -1
        for line in f:
            # считаем строки для создания списка
            i += 1
            # уберём перенос строки
            line = line.replace('\n', '')
            # разделяем предмет и оценки
            line = line.split(':')

            subject = line[0]
            if sub == subject:
                grades = line[1].split(',')
                grades = grades[:-1]
    return grades



# отладка
if __name__ == "__main__":
    # name = 'Potap'
    # # base_init(name)
    data = export_performance('Potap')
    # print(data)
    data = edit_performance(data, 'Math', '3')
    # print(data)
    import_performance(data, 'Potap')
