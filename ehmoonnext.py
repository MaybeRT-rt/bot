import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from mybot import start_user
import ephem as ep


logging.basicConfig(filename="bot.log", format='%(levelname)s -%(asctime)s -%(message)s', level=logging.INFO) 


def next_full_moon(update, context):
    moon = update.message.text.split()[1]
    moon = moon.replace('.', '/')
    moon_next = ep.next_full_moon(moon)
    update.message.reply_text(f' Ближайшее полнолуние: {moon_next}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))



    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

