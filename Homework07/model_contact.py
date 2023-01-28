
# * поверхностный функционал по работе с файлами

import model_work_files as wf


# импорт контактов
def import_contact(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# экспорт контактов
def export_contact(path):
    temp_export = []
    with open(path, "r") as file:
        for line in file:
            # уберём переносы строк
            line = line.replace('\n', '')
            # преобразуем в список
            line = line.split(';')
            temp_export.append(line)

    # for value in temp_export:
    #     print('s'+value)
    
    # data = wf.read_file_txt(path)
    return temp_export


# есть ли книга с контактами?
def get_contact_book(path):
    return 0


# создадим книгу с контактами
def create_contact_book(path):
    wf.create_file_txt(path, '')



# отладка
if __name__ == "__main__":
    a = export_contact('contact.txt')

    print(a[0][0])
