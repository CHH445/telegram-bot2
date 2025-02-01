import telebot

# Deinen Bot-Token hier einfügen!
TOKEN = "7578687524:AAEYdO9F4HfnmM4wj4u4fBD8ObIb1DJi7ds"
bot = telebot.TeleBot(TOKEN)

# /start-Befehl
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hallo! Ich bin dein Telegram-Bot. Schreibe /hilfe für eine Liste der Befehle.")

# /hilfe-Befehl
@bot.message_handler(commands=["hilfe"])
def send_help(message):
    bot.reply_to(message, "Verfügbare Befehle:\n/start - Startet den Bot\n/hilfe - Zeigt diese Hilfe\n/info - Zeigt Infos")

# /info-Befehl
@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "Dieser Bot wurde erstellt, um dir zu helfen! 😊")

# Automatische Antworten auf bestimmte Wörter
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()
    if "hallo" in text:
        bot.reply_to(message, "Hallo! Wie kann ich dir helfen?")
    elif "danke" in text:
        bot.reply_to(message, "Gerne! 😊")
    elif "hilfe" in text:
        bot.reply_to(message, "Brauchst du Hilfe? Schreibe /hilfe für eine Liste der Befehle!")

# Bot starten
print("Bot läuft...")
bot.infinity_polling()
