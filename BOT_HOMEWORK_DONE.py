
"""
ДЗ
В этот раз задача следующая - используя то, чему научились, поработаем с нашим ботом.
Что нам понадобиться?
Тезисы из лекции по работе с  TelegramBotApi
-  Бот это сущность, которую создает Телеграмм и дает нам возможность управлять им с помощью веб-апи. 
- Веб-апи это набор  url- аддресов через которые можно послать или получать информацию. Для каждого  бота эти адреса уникальны потому, чо в них используется токен бота - его секретное обозначение
- На эти адреса (они называются эндпоинты) ходить можно двумя способами - что-то БРАТЬ или что-то ДАВАТЬ, это два МЕТОДА ЗАПРОСА -  GET  и POST
- GET это метод по умолчанию, он работает, когда мы просо переходим на стпничку и получаем в ответ данные
- POST позволяет данные отправить, но для этого к запросу надо прикрепить их в виде ТЕЛА ЗАПРОСА

Соответственно, зная уникальный токен вашего бота и зная шаблоны  url-адресов, через которые им можно управлять, можно, используя библиотеку  requests, манипулировать, как угодно.

Официальная документация(англ.), полная, но может быть немого непонятно- https://core.telegram.org/bots/api
Болуу проста и доступная документация на русском - https://tlgrm.ru/docs/bots/api

Ключевой момент - построение адреса
https://api.telegram.org/bot<ваш токен полученный при регистрации бота>/ <метод - getMe getUpdates sendMessage>
Например
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe

Работая с ним и правильно используя POST и GET все получиться

Вот здесь про метод POST для библиотеки REQUESTS
https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests
Как зарегистрировать бота:
https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram/


#1
Самое базовое - написать функцию, принимающую в качестве аргумента текст сообщения и отправляющую его от бота в чат к пользователю. chat_id можно захардкодить

#2
Тут чуть посложнее - сделать функцию  посыла сообщения, принимающую в качестве аргумента  chat_id и текст сообщения.
А так же функцию, извлекающую  chat_id  из последнего сообщения, отправленного боту.  Получить его можно используя метод getUpdates - разобрать полученный Джон. Вытащить список сообщений, извлечь из него последнее, а из него - данные о чате. Тут не столько сложная задача, сколько сам ответ, содержащий апдейты большой, и нужно будет вспомнить, как извлекать данные из словарей и спинов, вложенных друг в друга.

#3
Написать эхо-бота - скрипт, который, при запуске, отсматривает последнее сообщение, и в пересылает его же в чат с юзером, отправившим это сообщение

#4 
Написать скрипт, проверяющий последнее сообщение, и, если в нем есть запрос на курс валют, как в прошлом домашнем задании (запрос на курс по дате, на динамику изменил и т.д) то отправлять ему, через бота, сообщение с реузльтатм выполнения скрипта, работающего по курсам. То есть, результат прошлого ДЗ не просо выводить на экран, а отсылать в телеге через бота.
"""
import requests

import json

# s = "<p>\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c,</p>"
# x = s.encode('utf-8')
# x.decode('utf-8')

l_currency = ["EUR", "USD", "RUB"]

currency = {"EUR": 292, "USD": 145, "RUB": 298}

cur_id = currency["USD"]

c_date = ["2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04", "2020-12-05", "2020-12-06", "2020-12-07", "2020-12-08", "2020-12-09", "2020-12-10" ,"2020-12-11", "2020-12-12", "2020-12-13", "2020-12-14"]

x = 14

ok_codes = (200, 201, 202)

token = "1387500601:AAG1aLzoOY1lv4sstK5yOcvN9aChnaXTMyM"

text = f'Добрейший денёчек!'

result = requests.post("https://api.telegram.org/bot1387500601:AAG1aLzoOY1lv4sstK5yOcvN9aChnaXTMyM/getUpdates")

getUpdates = result.__dict__

last_message = json.loads(getUpdates['_content'])['result'][-1]['message']['text']

def m_bank(message):

	curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_date}"
	response = requests.get(curr_url)
	status = response.status_code	

	if status in ok_codes:

		if message == f"Динамика курса за {x} дней":

			rates = []
			culc_rates = []

			for c_d in c_date:

				url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_d}"
				my_response = requests.get(url).json()
				cur_rate = my_response['Cur_OfficialRate'] 
				rates.append(cur_rate)


			for val in rates[:-1]:
				culc_rates.append(val - rates[rates.index(val) + 1])


			cur_message = f"Динамика изменения {l_currency[1]} за {str(x)} дней:"

			for c_d, culc in zip(c_date, culc_rates):

				curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_d}"
				response = requests.get(curr_url)
				curr = response.json()
				date = (curr['Date'].replace("T00:00:00", ""))

				cur_message += f"\n {date}: {culc} "

			return cur_message

		if message == f"Курс USD на сегодня":

			date = c_date[-1]
			url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={date}"
			response = requests.get(url)

			return f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

		if message == f"Курс USD на вчера":

			date = c_date[-2]
			url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={date}"
			response = requests.get(url)

			return f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

		if message == f"Курс валют EUR USD RUB на сегодня":

			date = c_date[-1]
			message = f"Курс запрошенных валют на {date} составляет"

			for l_c in l_currency:

				c = currency[l_c]
				url = f"https://www.nbrb.by/api/exrates/rates/{c}?ondate={date}"
				response = requests.get(url)
				message += f"\n за {response.json()['Cur_Scale']} {response.json()['Cur_Name']}: {response.json()['Cur_OfficialRate']} белорусских рублей "

			return message
	else:
		return f"Соедининение не удалось, мы получили ответ {status}"


def id(getUpdates):

 	chat_id = json.loads(getUpdates['_content'])['result'][0]['message']['chat']['id']
 	return chat_id


chat_id = id(getUpdates)

def message(text, chat_id, token):

	return requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data = {'chat_id' : chat_id, 'text': text})


message(last_message, chat_id, token)
message(m_bank(last_message), chat_id, token)

