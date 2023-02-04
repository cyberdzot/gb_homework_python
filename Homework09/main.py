
# * 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв


from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

# токен бота
bot_token = ''

# набор букв для поиска
value_for_del = 'абв'


bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def is_sym_in_text(update, context):
    text = update.message.text
    words = text.split()
    for value in words:
        if value_for_del in value:
            words.remove(value)
    context.bot.send_message(update.effective_chat.id, ' '.join(words))


text_handler = MessageHandler(Filters.text, is_sym_in_text)
dispatcher.add_handler(text_handler)


updater.start_polling()
updater.idle()