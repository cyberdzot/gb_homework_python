
# * текст интерфейса

l_option_text = {
    'main': [
        'Кто входит в систему?',
        '',
        '',
        '',
        '',
        '[0] Учитель',
        '[1] Ученик',
        '[2] Выйти'
    ],
    'write_main': [
        'Ввод данных ученика.',
        '',
        '',
        'Фамилия: ',
        'Предмет: ',
        'Оценка: ',
        '',
        ''
    ],
    'write_succes': [
        'Оценка успешно записана!',
        '',
        '',
        'Фамилия: ',
        'Предмет: ',
        'Оценка: ',
        '',
        '[0] Главное меню'
    ],
    'read_main': [
        'Просмотр успеваемости ученика.',
        '',
        '',
        'Фамилия: ',
        'Предмет: ',
        'Оценки: ',
        '',
        ''
    ],
    'read_succes': [
        'Успеваемость ученика выгружена.',
        '',
        '',
        'Фамилия: ',
        'Предмет: ',
        'Оценки: ',
        '',
        '[0] Главное меню'
    ]}


def get_dialog_text(d_key, line):
    return l_option_text[d_key][line]
