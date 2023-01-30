
# * скелет интерфейса

# from logger import add_action_log as log


# вывод в терминал
def view(data):
    # log('ui_view', data)
    print(data)

# ввод через терминал
def get_value(before = '\nВведите вариант ответа: '):
    a = input(before)
    # log('ui_get_value', before + ' ' + a)
    return a

# очистка терминала
def clear():
    print("\033[H\033[J")


#################################
# начальный key который будет нас встречать
dialog = 'main'

l_option = {
    'main':         ['write_main', 'read_main', 'exit'],
    'write_succes': ['main'],
    'read_succes':  ['main']
}


# узнать текущий диалог
def get_dialog():
    global dialog
    return dialog

# выбрать диалог
def set_dialog(d_key):
    global dialog
    dialog = d_key

# узнать доступный диалог в выбранном диалоге
def get_dialog_from_key(d_key, id_key):
    return l_option[d_key][id_key]

# узнать количество доступных диалогов в выбранном диалоге
def get_len_dialog_from_key(d_key):
    return len(l_option[d_key])
#################################



# отладка
if __name__ == "__main__":
    view('data123')