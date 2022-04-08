
import logging
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('I AM ALIVE!')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not smart enough to help you, but maybe try /commands.')

def time(update, context):
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    update.message.reply_text("The date and time is currently: " + dt_string)

def commands(update, context):
    bot_start = "/start"
    bot_help = "/help"
    bot_time = "/time"
    update.message.reply_text(bot_start + "\n" + bot_help + "\n" + bot_time)

def quip(update, context):
    if len(update.message.text) > 15:
        update.message.reply_text("What you have just told me will be our secret.")
    else:
        echo(update, context)

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + ', interesting, you should tell me more about yourself.')

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5170821358:AAHdXJ6h-72bjWnMvHrv2P88zckhu6pvtHI", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time",time))
    dp.add_handler(CommandHandler("commands",commands))

    dp.add_handler(MessageHandler(Filters.text, quip))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()