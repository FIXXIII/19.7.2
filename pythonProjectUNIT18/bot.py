import requests
import json
import config
import telebot

bot = telebot.TeleBot(config.token)

class APIException(Exception):
    def __init__(self, message):
        self.message = message

@bot.message_handler(commands=['start', 'help'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Введите команду в формате: \n<имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>')

@bot.message_handler(commands=['values'])
def values_handler(message):
    currencies = 'Доступные валюты: \n'
    for key in CURRENCY.keys():
        currencies += key + ' - ' + CURRENCY[key] + '\n'
    bot.send_message(message.chat.id, currencies)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Неверное количество параметров')
        base = values[0].upper()
        quote = values[1].upper()
        amount = float(values[2])
        result = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка: {e.message}')
        return
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {str(e)}')
        return
    bot.send_message(message.chat.id, result)

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if base not in CURRENCY or quote not in CURRENCY:
            raise APIException('Неверное название валюты')
        response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}')
        if response.status_code != 200:
            raise APIException('Ошибка запроса курса валют')
        data = json.loads(response.text)
        rate = data['rates'][quote]
        result = rate * amount
        return f'{amount:.2f} {CURRENCY[base]} = {result:.2f} {CURRENCY[quote]}'

CURRENCY = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'RUB': 'Российский рубль'
}
