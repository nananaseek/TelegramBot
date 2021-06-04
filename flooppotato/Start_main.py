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


# Реестрирует пользователя когда тот обращается к боту командой /start
def do_start(update: Update, context: CallbackContext):
    user = update.effective_user

    add_user(
        user_id=user.id,
    )
    update.message.reply_text(
        text="Бот починає свою роботу, через деякий час вам буде надіслане перше слово :з",
    )


def do_search(update: Update, context: CallbackContext):
    text = update.effective_message.text
    try:
        update.message.reply_text(
            text=searchE(word=text),
        )
    except:
        update.message.reply_text(
            text=searchU(word=text),
        )


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
    message_handlerE = MessageHandler(Filters.text, do_search)

    updater.dispatcher.add_handler(message_handlerE)
    updater.dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
