
# * логирование

from datetime import datetime
from os.path import exists, join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
COL_NAMES = ('Время', 'ID пользователя', 'Пример', 'Результат')
FORMAT_DATETIME = '%H:%M:%S'


def logging(user_id: str, data: str, result: str,
            file_path: str = 'log') -> None:
    time = datetime.now().strftime(FORMAT_DATETIME)
    user_id = str(user_id)
    result = str(result)
    log_path = join(BASE_DIR, file_path + '.csv')

    if not exists(log_path):
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(', '.join(COL_NAMES) + '\n')

    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f'{time}, {user_id}, {data}, {result}\n')


def show_log(file_path: str = 'log') -> list:
    log_path = join(BASE_DIR, file_path + '.csv')

    if not exists(log_path):
        return []

    with open(log_path, 'r', encoding='utf-8') as f:
        logs = f.readlines()
        for i in range(len(logs)):
            logs[i] = logs[i].strip('\n').split(', ')

    return logs
