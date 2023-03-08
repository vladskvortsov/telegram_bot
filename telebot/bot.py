import telebot, os#, time
from telebot import TeleBot, types
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter


TOKEN = os.environ['TELEGRAM_TOKEN']


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добрий вечір")




@bot.message_handler(text=TextFilter(contains=['Вибухи', 'вибухи']))
def contains_handler(message: types.Message):
#    bot.send_message(message.chat.id, 'Так, дійсно вибухи')
    bot.reply_to(message, 'Так, дійсно вибухи')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'Слава Україні':
        bot.send_message(message.chat.id, 'Героям слава!')
#        time.sleep(2)
        bot.send_message(message.chat.id, 'І смерть клятим ворогам!!!')
    elif message.text == 'Glory for Ukraine':
        bot.send_message(message.chat.id, 'Glory for heroes!!!')
    else:
        bot.reply_to(message, message.text)












if __name__ == '__main__':
    bot.add_custom_filter(TextMatchFilter())
    bot.add_custom_filter(IsReplyFilter())
    bot.infinity_polling()
