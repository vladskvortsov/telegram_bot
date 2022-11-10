# -*- coding: utf-8 -*-
import telebot
from telebot import TeleBot, types
from telebot.custom_filters import TextFilter, TextMatchFilter

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
        bot.send_message(message.chat.id, 'Glory for heroes!')
    elif message.text == 'Glory':
        bot.send_message(message, 'Glory for heroes!!!')
    else:
        bot.reply_to(message, message.text)



















@bot.message_handler(text=TextFilter(contains=['Вибухи', 'вибухи']))
def contains_handler(message: types.Message):
    bot.reply_to(message, 'Так, дійсно вибухи')





if __name__ == '__main__':
    bot.add_custom_filter(TextMatchFilter())
    bot.infinity_polling(none_stop=True)
