from mybot import start_user
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", format='%(levelname)s -%(asctime)s -%(message)s', level=logging.INFO) 


def wordcount(update, context):
    first_name = update.message.chat.first_name
    text = update.message.text
    for i in '\n_': 
        text = text.replace(i, ' ')
    lines = (len(text.split(' '))) -1
    if not lines:
        update.message.reply_text(f'{first_name}, Вы ввели пустую строку')
    if lines == 1:
        update.message.reply_text(f'{lines} слово')
    elif 2 <= lines < 5:
        update.message.reply_text(f'{lines} слова')
    elif lines >= 5:
        update.message.reply_text(f'{lines} слов')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()