import telebot
from info import keys, T
from extensions import Converter
from extensions import Exceptions

bot = telebot.TeleBot(T)

@bot.message_handler(commands=['start', 'help'])
def handler_start_help(mes):
    bot.send_message(mes.chat.id, "Привет! Я бот для конвертации валют.\nЧтобы перевести одну валюту в другую напишите:"
                                  "\n<имя валюты>  <имя валюты, в которую надо перевести>  <количество первой "
                                  "валюты>\n\nНажмите /values, чтобы посмотреть доступные валюты")

@bot.message_handler(commands=['values'])
def handler_values(mes):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = text + '\n' + key
    bot.send_message(mes.chat.id, text)


@bot.message_handler(content_types=['text'])
def handler_text(mes):
    values = mes.text.split()

    try:
        if len(values) != 3:
            raise Exceptions('Неверное количество параметров! Введите 3 параметра.')
        base, quote, amount = values
        answer = Converter().convert(base, quote, amount)

    except Exceptions as e:
        bot.reply_to(mes, f"Не удалось обработать команду:\n{e}")

    else:
        bot.send_message(mes.chat.id, answer)

bot.polling(none_stop=True)