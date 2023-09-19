import telebot as tb
from telebot import types 
bot = tb.TeleBot("6552314614:AAGIyc9637YBVmHGDUwAVEG0w6Z2gI-O5Qk", parse_mode=None)

@bot.message_handler(commands = ['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup())
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n\nDrama\'s bot представляет вам возможность ментально закопать себя в яму. Для продолжения выбери один из пунктов.', reply_markup=markup)
    
@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, 'Помощь в решении техничеких проблем - @Dramanono')


@bot.message_handler(commands = ['creators'])
def main(message):
    bot.send_message(message.chat.id, 'Создатели бота - @Dramanono и @ArkonStone')


@bot.message_handler(commands = ['generate text'])
def main(message):
    pass


@bot.message_handler(commands = ['music'])
def main(message):
    pass


@bot.message_handler(commands = ['donate'])
def main(message):
    pass

bot.polling(none_stop=True)