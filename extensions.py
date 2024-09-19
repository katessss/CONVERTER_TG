import requests
import json
from info import keys

class Exceptions(Exception):
    pass

class Converter:
    def convert(self, base, quote, amount):

        #Возможные ошибки ввода

        try:
            keys[base.lower()] and keys[quote.lower()]
        except KeyError:
            raise Exceptions('Введите валюты из списка /values')

        try:
            float(amount)
        except ValueError:
            raise Exceptions("Введите последний параметр в виде числа")

        if base == quote:
            raise Exceptions('Нельзя конветировать валюту саму в себя!')

        link = 'https://min-api.cryptocompare.com/data/price?fsym=' + keys[base.lower()] + '&tsyms=' + keys[quote.lower()]
        res = json.loads(requests.get(link).content)
        for i in res:
            answer = f"{amount} {keys[base.lower()]} = {str(float(amount) * res[i])} {keys[quote.lower()]}"

        return answer
