
# * контроллер


# from logger import add_action_log as log
import user_interface as ui
import user_interface_text as ui_text
import data_base as db


VERSION             = '0.1'

# фамилия * имя * предмет * оценка
add_info = {'nam': '', 'sub': '', 'gra': ''}



def clear_temp_info():
    add_info['nam'] = ''
    add_info['sub'] = ''
    add_info['gra'] = ''


def show_title():
    ui.clear()
    ui.view('----------------------------------')
    ui.view('  Табель успеваемости (ver. {}) '.format(VERSION))
    ui.view('----------------------------------\n')


def ui_all_update(d_key):
    show_title()
    ui.view(ui_text.get_dialog_text(d_key, 0))
    ui.view(ui_text.get_dialog_text(d_key, 1))
    ui.view(ui_text.get_dialog_text(d_key, 2))
    ui.view(ui_text.get_dialog_text(d_key, 3) + add_info['nam'])
    ui.view(ui_text.get_dialog_text(d_key, 4) + add_info['sub'])
    ui.view(ui_text.get_dialog_text(d_key, 5) + add_info['gra'])
    ui.view(ui_text.get_dialog_text(d_key, 6))
    ui.view(ui_text.get_dialog_text(d_key, 7))


def main_update(d_key):
    ui_all_update(d_key)
    # регулируем запись
    if d_key == 'write_main':
        add_info['nam'] = ui.get_value('Введите фамилию: ')
        ui_all_update(d_key)
        add_info['sub'] = ui.get_value('Введите предмет: ')
        ui_all_update(d_key)
        add_info['gra'] = ui.get_value('Введите оценку: ')
        ui.set_dialog('write_succes')
        db.write(add_info['nam'], add_info['sub'], add_info['gra'])
    # регулируем чтение
    elif d_key == 'read_main':
        add_info['nam'] = ui.get_value('Введите фамилию: ')
        ui_all_update(d_key)
        add_info['sub'] = ui.get_value('Введите предмет: ')
        ui_all_update(d_key)
        gra_list = db.read(add_info['nam'], add_info['sub'])
        for value in gra_list:
            add_info['gra'] += value + ' '
        ui.set_dialog('read_succes')
    else:
        opt = ui.get_value()
        opt = int(opt)
        if ui.get_len_dialog_from_key(d_key) - 1 >= opt:
            next_d_key = ui.get_dialog_from_key(d_key, opt)
            ui.set_dialog(next_d_key)
            if d_key == 'write_succes' or d_key == 'read_succes':
                clear_temp_info()

def start():
    while True:
        d_key = ui.get_dialog()
        if d_key == 'exit':
            show_title()
            ui.view('Вы завершили работу с табелем успеваемости.')
            ui.view('')
            break
        main_update(d_key)


# отладка
if __name__ == "__main__":
    start()
