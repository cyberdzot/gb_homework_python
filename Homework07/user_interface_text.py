
# * текст интерфейса

l_option_text = {
    'main': [
        'Что будем делать с контактами?',
        '',
        '',
        '',
        '',
        '[0] Выйти',
        '[1] Записать новый',
        '[2] Показать имеющиеся'
    ],
    'write_succes': [
        'Контакт успешно записан!',
        '',
        'Фамилия: ',
        'Имя: ',
        'Телефон: ',
        'Описание: ',
        '',
        '[0] Главное меню'
    ],
    'write_main': [
        'Запись контакта.',
        '',
        'Фамилия: ',
        'Имя: ',
        'Телефон: ',
        'Описание: ',
        '',
        ''
    ],
    'read_main': [
        'Чтение контакта.',
        '',
        'Фамилия: ',
        'Имя: ',
        'Телефон: ',
        'Описание: ',
        '[0] Главное меню',
        '[1] Далее'
    ],
    'read_succes': [
        'Чтение контакта.',
        'Контактов больше нет!',
        '',
        '',
        '',
        '',
        '',
        '[0] Главное меню'
    ]}


def get_dialog_text(d_key, line):
    return l_option_text[d_key][line]




