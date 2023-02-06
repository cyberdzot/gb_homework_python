
# * обработчики всего и вся =)

from telegram import Update
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackContext,
                          ConversationHandler)

from calculator import process_func
from logger import logging, show_log


STATES = (0, 1, 2)


def start(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(update.effective_chat.id,
                             'Вы запустили калькулятор.')
    context.bot.send_message(update.effective_chat.id,
                             'Выберите действие:\n\t1. Калькулятор\
\n\t2. Последние действия\nЛюбой другой ввод - завершает диалог!')
    return STATES[0]


def menu(update: Update, context: CallbackContext) -> int:
    msg_data = update.message.text

    if msg_data == '1':
        context.bot.send_message(update.effective_chat.id,
                                 'Вы выбрали калькулятор\n\
Введите выражение без скобок и отрицательных чисел\nПример: 12+3*3')
        return STATES[1]

    elif msg_data == '2':
        context.bot.send_message(update.effective_chat.id,
                                 'Вы выбрали просмотр последних действий\n\
Введите количество записей, которые вы желаете посмотреть')
        return STATES[2]

    else:
        context.bot.send_message(update.effective_chat.id,
                                 'Прощаемся!')
        return ConversationHandler.END


def calculator(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    msg_data = update.message.text
    result = str(process_func(msg_data))
    
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')
    logging(user_id, msg_data, result)
    context.bot.send_message(update.effective_chat.id,
                             'Выберите действие:\n   1. Калькулятор\
\n   2. Последние действия\n\nЛюбой другой ввод - завершает диалог!')

    return STATES[0]


def last_logs(update: Update, context: CallbackContext) -> int:
    logs_cnt = int(update.message.text)
    log = show_log()
    if log:
        cols = log[0]
        log = log[1:]

    if logs_cnt > 0 and logs_cnt <= len(log):
        for log in log[-logs_cnt:]:
            msg_text = []

            for i in range(len(log)):
                msg_text.append(f'{cols[i]}: {log[i]}')

            msg_text = '\n'.join(msg_text)
            context.bot.send_message(update.effective_chat.id, msg_text)

    if len(log) < 1:
        context.bot.send_message(update.effective_chat.id,
                                 'В журнале пока нет записей!')

    elif logs_cnt > len(log):
        context.bot.send_message(update.effective_chat.id,
                                 f'В журнале всего {len(log)} записей!')

    context.bot.send_message(update.effective_chat.id,
                             'Выберите действие:\n\t1. Калькулятор\
\n\t2. Последние действия\nЛюбой другой ввод - выводит из диалога!')

    return STATES[0]


def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Работа закончена.')


start_handler = CommandHandler('start', start)
menu_handler = MessageHandler(Filters.text, menu)
calculator_handler = MessageHandler(Filters.text, calculator)
last_logs_handler = MessageHandler(Filters.text, last_logs)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       STATES[0]: [menu_handler],
                                       STATES[1]: [calculator_handler],
                                       STATES[2]: [last_logs_handler]
},
    fallbacks=[cancel_handler])
