
# * контроллер


import logger as log
import user_interface as ui
import user_interface_text as ui_text
import model_contact as mc
# import os.path

VERSION = '0.1'
PATH_CONTACT_BOOK = 'contact.txt'

add_contact = {'fam': '', 'nam': '', 'tel': '', 'des': ''}


def show_title():
    ui.clear()
    ui.view('----------------------------------')
    ui.view(f' Телефонный справочник (ver. {VERSION}) ')
    ui.view('----------------------------------\n')


def ui_all_update(d_key):
    show_title()
    ui.view(ui_text.get_dialog_text(d_key, 0))
    ui.view(ui_text.get_dialog_text(d_key, 1))
    ui.view(ui_text.get_dialog_text(d_key, 2) + add_contact['fam'])
    ui.view(ui_text.get_dialog_text(d_key, 3) + add_contact['nam'])
    ui.view(ui_text.get_dialog_text(d_key, 4) + add_contact['tel'])
    ui.view(ui_text.get_dialog_text(d_key, 5) + add_contact['des'])
    ui.view(ui_text.get_dialog_text(d_key, 6))
    ui.view(ui_text.get_dialog_text(d_key, 7))


def clear_temp_contact():
    add_contact['fam'] = ''
    add_contact['nam'] = ''
    add_contact['tel'] = ''
    add_contact['des'] = ''


def start():
    # if not os.path.exists(PATH_CONTACT_BOOK):
    #     mc.create_contact_book(PATH_CONTACT_BOOK)
    #
    while True:
        d_key = ui.get_dialog()
        if d_key == 'exit':
            show_title()
            ui.view('Вы закрыли справочник. До встречи.')
            ui.view('')
            break
        update(d_key)


def update(d_key):
    ui_all_update(d_key)

    # если зашли в запись
    if d_key == 'write_main':
        add_contact['fam'] = ui.get_value('Введите фамилию: ')
        ui_all_update(d_key)
        add_contact['nam'] = ui.get_value('Введите имя: ')
        ui_all_update(d_key)
        add_contact['tel'] = ui.get_value('Введите телефон: ')
        ui_all_update(d_key)
        add_contact['des'] = ui.get_value('Введите описание: ')
        ui_all_update(d_key)
        #
        ui.set_dialog('write_succes')
        mc.import_contact(
            PATH_CONTACT_BOOK, add_contact['fam']+';'+add_contact['nam']+';'+add_contact['tel']+';'+add_contact['des'])

    # если зашли в чтение
    elif d_key == 'read_main':
        contact_cache = mc.export_contact(PATH_CONTACT_BOOK)
        step = ui.get_current_read_contact()
        add_contact['fam'] = contact_cache[step][0]
        add_contact['nam'] = contact_cache[step][1]
        add_contact['tel'] = contact_cache[step][2]
        add_contact['des'] = contact_cache[step][3]
        ui_all_update(d_key)
        # собираем варианты ответов
        opt = ui.get_value()
        opt = int(opt)
        # если введём существующий вариант диалога
        if ui.get_len_dialog_from_key(d_key) - 1 >= opt:
            # log.add_action_log('contr', f'{len(contact_cache)} {step}')
            if step >= len(contact_cache) - 1:
                next_d_key = 'read_succes'
            else:
                next_d_key = ui.get_dialog_from_key(d_key, opt)
            #
            ui.set_dialog(next_d_key)
            if next_d_key == d_key:
                ui.set_current_read_contact(step + 1)
            else:
                ui.set_current_read_contact(0)
                clear_temp_contact()

    else:
        # собираем варианты ответов
        opt = ui.get_value()
        opt = int(opt)

        # если введём существующий вариант диалога
        if ui.get_len_dialog_from_key(d_key) - 1 >= opt:
            next_d_key = ui.get_dialog_from_key(d_key, opt)
            ui.set_dialog(next_d_key)
            # если мы в диалоге об успешной записи контакта
            if d_key == 'write_succes':
                clear_temp_contact()


# отладка
if __name__ == "__main__":
    start()

# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1

# Фамилия_1,Имя_1,Телефон_1,Описание_1
