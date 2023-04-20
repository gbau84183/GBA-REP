import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the callback function for the /start command
def start(update: Update, _: CallbackContext) -> None:
    buttons = [[KeyboardButton('Option 1'), KeyboardButton('Option 2'), KeyboardButton('Option 3')]]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text('Welcome to the voting bot! Please choose one of the options below:', reply_markup=reply_markup)

# Define the callback function for user votes
def vote(update: Update, _: CallbackContext) -> None:
    selected_option = update.message.text
    # TODO: Save the vote to a database or file
    update.message.reply_text(f"You voted for {selected_option}. Thank you for voting!")

# Set up the bot
def main() -> None:
    # Set up the bot and add your command handlers
    updater = Updater("YOUR_TOKEN_HERE")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & (Filters.regex('^Option 1$') | Filters.regex('^Option 2$') | Filters.regex('^Option 3$'))), vote)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
