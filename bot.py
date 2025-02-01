import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token einfügen
BOT_TOKEN = "7578687524:AAEYdO9F4HfnmM4wj4u4fBD8ObIb1DJi7ds"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    # Nachricht senden
    text = "This Is The Official Binance Loan Bot.\nSelect “CLICK HERE TO GET LOAN” To Get Started\n\n🔝 Main Menu"
    bot.send_message(chat_id, text, reply_markup=main_menu())

# Funktion für das Hauptmenü
def main_menu():
    markup = InlineKeyboardMarkup()
    
    btn_loan = InlineKeyboardButton("✅ Click here to get Loan", callback_data="get_loan")
    btn_support = InlineKeyboardButton("💬 Support", callback_data="support")
    btn_announcement = InlineKeyboardButton("📢 Announcement", callback_data="announcement")

    markup.add(btn_loan)
    markup.add(btn_support, btn_announcement)

    return markup

# Callback-Funktion für die Buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get_loan":
        bot.send_message(call.message.chat.id, "🔹 You selected: Get Loan\n\n➡ Please enter the loan amount.")
    elif call.data == "support":
        bot.send_message(call.message.chat.id, "🔹 You selected: Support\n\n📞 Contact us at @SupportUsername")
    elif call.data == "announcement":
        bot.send_message(call.message.chat.id, "🔹 Latest Announcements:\n\n🚀 New features coming soon!")

# Bot starten
bot.polling()
