from telegram import Bot
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

from flooppotato.db import twenty_two
from flooppotato.config import TG_TOKEN
from flooppotato.db_quest import con_first_q
from flooppotato.db_quest import con_second_q
from flooppotato.db_quest import con_test_q
from flooppotato.db_quest import random_quest
from flooppotato.db_quest import init_db

import schedule
import time
import os.path

bot = Bot(
    token=TG_TOKEN,
)
updater = Updater(
    bot=bot,
    use_context=True,
)
random_quest = random_quest


def config_fq(random_quest):
    random_quest = int(random_quest)
    (one,) = con_first_q[random_quest]
    return one


def config_sq(random_quest):
    random_quest = int(random_quest)
    (two,) = con_second_q[random_quest]
    return two


def config_tq(random_quest):
    random_quest = int(random_quest)
    (three,) = con_test_q[random_quest]
    return three


config_fq = config_fq(random_quest)
config_sq = config_sq(random_quest)
config_tq = config_tq(random_quest)


# Отсыланеие сообщеня пльзователю в дневное время
def do_echo_morning(bot: Bot, updater: Updater):
    for chats in twenty_two:
        (chats,) = chats
        bot.send_message(
            chat_id=chats,
            text=config_fq,
        )


# в середине дня
def do_echo_day(bot: Bot, updater: Updater):
    for chats in twenty_two:
        (chats,) = chats
        bot.send_message(
            chat_id=chats,
            text=config_sq,
        )


# Отсылане проверочного сообщения
def do_echo_test(bot: Bot, updater: Updater):
    for chats in twenty_two:
        (chats,) = chats
        bot.send_message(
            chat_id=chats,
            text="penis",
        )


def creat_q():
    """
    Отлов повторяющихся сообщений
    """
    for chats in twenty_two:
        (chats,) = chats

        def wr(chats):
            chats = str(chats)
            if os.path.exists('Telegram users/' + chats) is True:
                f = open('Telegram users/' + chats, 'r')
                openF = f.read().splitlines()
                if random_quest not in openF:
                    f = open('Telegram users/' + chats, 'a')
                    f.write(random_quest + '\n')
                    f.close()
                f.close()
            else:
                f = open('Telegram users/' + chats, 'w')
                f.write(random_quest + '\n')
                print('file is add')
                f.close()

        wr(chats)


# Планировка отсылания сообщения
schedule.every(5).seconds.do(do_echo_test, bot, updater)
schedule.every(5).seconds.do(creat_q)


# schedule.every().day.at('01:00').do(creat_q)
# schedule.every().day.at('09:15').do(do_echo_morning, bot, updater)
# schedule.every().day.at('16:45').do(do_echo_day, bot, updater)
# schedule.every().day.at('19:27').do(do_echo_test, bot, updater)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

    init_db()
    message_handler = MessageHandler(Filters.text, do_search)

    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
