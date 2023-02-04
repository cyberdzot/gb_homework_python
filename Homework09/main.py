
# * 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв


from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

# токен бота
BOT_TOKEN = ''

# набор букв для поиска
VALUE_FOR_DEL = 'абв'


bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


def is_sym_in_text(update, context):
    text = update.message.text
    words = text.split()
    for value in words:
        if VALUE_FOR_DEL in value:
            words.remove(value)
    context.bot.send_message(update.effective_chat.id, ' '.join(words))


text_handler = MessageHandler(Filters.text, is_sym_in_text)
dispatcher.add_handler(text_handler)


updater.start_polling()
updater.idle()