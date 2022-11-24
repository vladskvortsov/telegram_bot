import telebot, time
from telebot import TeleBot, types
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter


TOKEN = None

with open("token") as f:
    TOKEN = f.read().strip()

#def lambda_handler(event, context):
    
    
bot = telebot.TeleBot(TOKEN)



 


 #@bot.message_handler(content_types=['text'])
 def lambda_handler(message):
    if message.text == 'Слава Україні':
        bot.send_message(message.chat.id, 'Героям слава!')
        time.sleep(2)
        bot.send_message(message.chat.id, 'І смерть клятим ворогам!!!')
    elif message.text == 'Glory for Ukraine':
        bot.send_message(message.chat.id, 'Glory for heroes!!!')
    else:
        bot.reply_to(message, message.text)



if __name__ == '__main__':
    bot.add_custom_filter(TextMatchFilter())
    bot.add_custom_filter(IsReplyFilter())
    bot.infinity_polling()
