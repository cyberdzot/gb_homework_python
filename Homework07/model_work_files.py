
# * коренной функционал по работе с файлами


# создадим файл если его нету или откроем текущий без удаления в нём данных
def create_file_txt(_dir, data):
    # "a+"
    my_file = open(_dir, "w+")
    my_file.write(data)
    my_file.close()


# считаем файл
def read_file_txt(_dir):
    my_file = open(_dir)
    output = my_file.read()
    my_file.close()
    return output