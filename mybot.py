import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem as ep

logging.basicConfig(filename="bot.log", format='%(levelname)s -%(asctime)s -%(message)s', level=logging.INFO) 


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

today = ('1996/12/04')
planet_dict = {
                'Saturn': ep.Saturn(today), 'Jupiter': ep.Jupiter(today),'Moon': ep.Moon(today),
                'Mars': ep.Mars(today), 'Venus': ep.Venus(today), 'Uranus': ep.Uranus(today),
                'Neptune': ep.Neptune(today), 'Sun': ep.Sun(today)
 }


def start_user(update, context):
    print('Вызван /start')
    update.message.reply_text("Здравствуй, пользователь!Ты вызывал команду /start")
    print(update)


def talk_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def  planet_start(update, context):
    planet_name = update.message.text.split()[1]
    ep_d = planet_dict.get(planet_name, None)
    if ep_d!=None:
        constellation = ep.constellation(planet_dict[planet_name])
        update.message.reply_text(constellation)
    else:
        update.message.reply_text('Я не знаю эту планету!')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("planet", planet_start))
    dp.add_handler(MessageHandler(Filters.text, talk_me))
    

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
