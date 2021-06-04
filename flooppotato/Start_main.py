from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

from flooppotato.db import init_db
from flooppotato.db import add_user
from flooppotato.config import TG_TOKEN
from flooppotato.dic_db import searchE
from flooppotato.dic_db import searchU
from flooppotato.dic_db import Check

from translator import go_translate


# Реестрирует пользователя когда тот обращается к боту командой /start
def do_start(update: Update, context: CallbackContext):
    user = update.effective_user

    add_user(
        user_id=user.id,
    )
    update.message.reply_text(
        text="Бот починає свою роботу, через деякий час вам буде надіслане перше слово :з",
    )


def do_trans(update: Update, context: CallbackContext):
    word = update.effective_message.text
    translate = go_translate(word)
    try:
        update.message.reply_text(
            text=translate,
        )
    except:
        update.message.reply_text(
            text=translate,
        )

    # eCheck = Check.eCheck()
    # ucheck = Check.uCheck()
    # text = update.effective_message.text
    # if text == 'P':
    #     if  text in ucheck:
    #         print(1)
    #     try:
    #         update.message.reply_text(
    #             text=searchE(word=text),
    #         )
    #     except:
    #         update.message.reply_text(
    #             text=searchU(word=text),
    #         )


def trans(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Чекаю на слово!!!",
    )
    do_trans()


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    init_db()

    start_handler = CommandHandler("start", do_start)
    testH = CommandHandler("t", trans)
    message_handlerE = MessageHandler(Filters.text, do_trans)

    updater.dispatcher.add_handler(testH)
    updater.dispatcher.add_handler(message_handlerE)
    updater.dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
