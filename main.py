import telebot

bot = telebot.TeleBot('5289484666:AAFmR8xGe8aKkDMf8yKIyoCbUC0XCbVNCts')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Python".format(
                         message.from_user))


@bot.message_handler(content_types=['text'])
def get_tetx_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Я тебя слышу! Ваше сообщение: " + ms_text)


bot.polling(none_stop=True, interval=0)
