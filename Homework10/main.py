
# * Создать калькулятор для работы с рациональными числами, организовать меню,
# * добавив в неё систему логирования (Содержит: id.Пользователь, ввод, результат)
# 12 + 3 * 3
# Ваш ответ: 21


from telegram import Bot
from telegram.ext import Updater

from handlers import conv_handler


BOT_TOKEN = ''

bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()