import telebot


#main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

bot.polling(none_stop=True)