from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# States for the conversation handler
SSN, URGENCY, COIN, AMOUNT = range(4)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Welcome to the Binance Loan Bot. Please click 'Get Loan' to start.",
        reply_markup=ReplyKeyboardMarkup([['Get Loan']], one_time_keyboard=True)
    )
    return SSN

def request_ssn(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Please enter your Social Security Number (SSN).")
    return URGENCY

def request_urgency(update: Update, context: CallbackContext) -> int:
    user_ssn = update.message.text
    context.user_data['ssn'] = user_ssn
    update.message.reply_text(
        "How urgent do you need the loan?",
        reply_markup=ReplyKeyboardMarkup([['Very Urgent', 'Not Urgent']], one_time_keyboard=True)
    )
    return COIN

def request_coin(update: Update, context: CallbackContext) -> int:
    user_urgency = update.message.text
    context.user_data['urgency'] = user_urgency
    update.message.reply_text(
        "Select your preferred cryptocurrency for the loan.",
        reply_markup=ReplyKeyboardMarkup([['BTC', 'ETH', 'SQL']], one_time_keyboard=True)
    )
    return AMOUNT

def request_amount(update: Update, context: CallbackContext) -> int:
    user_coin = update.message.text
    context.user_data['coin'] = user_coin
    update.message.reply_text(
        "Select the amount you wish to borrow.",
        reply_markup=ReplyKeyboardMarkup([['$1,000', '$10,000', '$50,000', '$100,000']], one_time_keyboard=True)
    )
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Loan request cancelled.")
    return ConversationHandler.END

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("7578687524:AAEYdO9F4HfnmM4wj4u4fBD8ObIb1DJi7ds", use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SSN: [MessageHandler(filters.TEXT & ~filters.COMMAND, request_ssn)],
            URGENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, request_urgency)],
            COIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, request_coin)],
            AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, request_amount)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
