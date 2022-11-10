import telebot


TOKEN = None

with open("token") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing?")


@bot.message_handler(content_types=['text'])
def echo_l(message):
    if message.text == 'Glory for Ukraine':
        bot.send_message(message.chat.id, 'Glory for heroes!!!')


bot.infinity_polling(none_stop=True)


