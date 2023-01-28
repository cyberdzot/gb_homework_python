
# * графический интерфейс

import logger as log


# вывод в терминал
def view(data):
    # log.add_action_log('ui_view', data)
    #
    print(data)

# ввод через терминал
def get_value(before = '\nВведите номер варианта: '):
    #
    a = input(before)
    # log.add_action_log('ui_get_value', before + ' ' + a)
    return a

# очистка терминала
def clear():
    print("\033[H\033[J")


# начальный key который будет нас встречать
dialog = 'main'

l_option = {
    'main':         ['exit', 'write_main', 'read_main'],
    'write_main':   ['main'],
    'write_succes': ['main'],
    'read_main':    ['main', 'read_main'],
    'read_succes':  ['main']
}


def get_dialog():
    global dialog
    return dialog


def set_dialog(key):
    global dialog
    dialog = key


def get_dialog_from_key(d_key, id_key):
    return l_option[d_key][id_key]


def get_len_dialog_from_key(d_key):
    return len(l_option[d_key])


cur_read_cont = 0

def get_current_read_contact():
    global cur_read_cont
    return cur_read_cont

def set_current_read_contact(value):
    global cur_read_cont
    cur_read_cont = value