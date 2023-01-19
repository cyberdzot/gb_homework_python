
# * Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

# "w+" сообщает, что запись будет осуществляться в новый файл. Если он существует, то новое содержимое нужно записать поверх уже существующего.
# Если же вместо этого использовать параметр "w", тогда файл будет создан только в том случае, если он не существовал до этого.
# Если нужно добавить новые данные в файл, тогда вместо "w+" нужно просто использовать параметр "a+".
# Однако в таком случае не будет добавлена новая строка, поэтому важно не забыть использовать символ \n.


DATA_FOR_TEST = "aaabbbbccbbbx"
ORIGINAL_FILE_DIR = "original.txt"
ENCODE_FILE_DIR = "encode.txt"
DECODE_FILE_DIR = "decode.txt"


# создадим файл
def create_file_txt(_dir, data):
    my_file = open(_dir, "w+")
    my_file.write(data)
    my_file.close()


# считаем файл
def read_file_txt(_dir):
    my_file = open(_dir)
    output = my_file.read()
    my_file.close()
    return output


def encode_data(data):
    new_data = ''
    char_old = data[0]
    count = 1

    _len = len(data)
    last_index = _len - 1

    for i in range(1, _len):
        char_new = data[i]

        if char_old != char_new:
            new_data = new_data + str(count) + char_old
            char_old = char_new
            count = 1
        else:
            count += 1

        if last_index == i:
            new_data = new_data + str(count) + char_old

    return new_data


def decode_data(data):
    new_data = ''

    last_index = len(data) - 1

    for i in range(0, last_index, +2):
        for j in range(int(data[i])):
            new_data = new_data + data[i + 1]
    return new_data


create_file_txt(ORIGINAL_FILE_DIR, DATA_FOR_TEST)
data_for_encode = read_file_txt(ORIGINAL_FILE_DIR)

en_data = encode_data(data_for_encode)

create_file_txt(ENCODE_FILE_DIR, en_data)
data_for_decode = read_file_txt(ENCODE_FILE_DIR)

de_data = decode_data(data_for_decode)
create_file_txt(DECODE_FILE_DIR, de_data)
