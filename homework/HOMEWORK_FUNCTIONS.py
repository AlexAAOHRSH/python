import requests

from random import randint

c_date = ["2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04", "2020-12-05", "2020-12-06", "2020-12-07", "2020-12-08"]

currency = {"EUR": 292, "USD": 145, "RUB": 298}

l_currency = ["EUR", "USD", "RUB"]

cur_id = currency["USD"]
curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_date}"

x = 8

ok_codes = (200, 201, 202)

# text = [f"Динамика курса за {x} дней", f"Курс {currency} на сегодня", f"Курс {currency} на {c_date}", f"Курс валют {l_currency} на сегодня"]

"""
В этом задани задача скомпановать все имеющиеся на даный момент знания и собрать из разрозненных кусочков один крепкий, работающий скрипт.
Наша певая веха - написать своего бота-помошника в телеге, и если работу с Телеграм АПИ мы не изучали, то вот написать часть мозгов для бота
вполне способный сейчас. 
Поэтому закончим с нашим валютным скриптом.

В качестве информации на вход у нас два словаря - даные о юзере
"""

user = {"username": "Алексей",
		"country": "BY"}

# и сообщение этого юзера. Сообщение в виде словаря, в котором описаны его поля.


user_message1 = {"user": user,
				"message_text":f"Динамика курса за {x} дней" ,
				"current_date":"2020-12-08"}

user_message2 = {"user": user,
				"message_text":f"Курс {currency} на сегодня" ,
				"current_date":"2020-12-08"}

user_message3 = {"user": user,
				"message_text":f"Курс {currency} на {c_date}" ,
				"current_date":"2020-12-08"}

user_message4 = {"user": user,
				"message_text":f"Курс валют {l_currency} на сегодня" ,
				"current_date":"2020-12-08"}



user_messages = [user_message1, user_message2, user_message3, user_message4]
"""
У нас должна быть функция, которая принимает два аргумента - user и user_message.
В зависимости от текста сообщения функция должна возвращать строку:

- Если спрашиваем про ДИНАМИКУ  курса,то возвращает строку с динамикой за указанную дату
- Если курс валюты на сегодня - курс валюты на сегодня
- Если курс валюты и дату - то курс за заднную дату
- Если курс нескольих валют на сегодня - то, соотетственно, сообщение с курсаи каждой указанной валюты.


Как именно правильно определять по тексту входящего сообщения, чкго же именно хочет юзер, не имея особого опыта рабты со строками?
Сейчас можно пойти на упрощение - предположить, что сообщение на каждую задачу строго в одном формате. 
Например просьба сообщть динамику ВСЕГДА будет выглядеть как  
'Динамика курса за Х дней' 
а запрос на курсы нескольких валют всегда будет
'Курсы валют на сегодня для ABBR,ABBR,ABBR'

Соответственно, остаеться только правильно извлечь нужные нам данные. из этой строки - например, из запроса о динамике колличество дней, 
за которые мы хотим увидеть динамику и, на ее основани, уже отсчитать даты назад.
А для запроса по конкретным валютам - вытащить из строки набор аббревиатур.

Что здесь может помочь?  
Например срезы - т.к строка это тоже последовательность, из нее так же можно извлекать элементы по индексу. И даже группы элементв. 
например, буквы с 1 по 5 ли же все буквы после 5.

О срезах:
https://pythonworld.ru/osnovy/indeksy-i-srezy.html
https://foxford.ru/wiki/informatika/srezy-spiskov-v-python


Кроме того можно использовать методы строк - поиск вхождений, подстроки ,етс. ЗДесь полезные ссылки с данными о метода строк:

https://ps.readthedocs.io/ru/latest/strings.html
https://www.bestprog.net/ru/2019/12/31/python-functions-based-on-searching-and-replacing-a-substring-in-a-string-ru/
https://otus.ru/nest/post/622/

Точно окажеться полезен метод split позволяющий преврать строку в список ,разбитый по опредленному разделителю
https://www.internet-technologies.ru/articles/razbienie-strok-cherez-split-v-python.html
"""


def m_bank(user, user_message):

	if user["country"] == "BY":

		curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_date}"
		response = requests.get(curr_url)
		status = response.status_code	

		if status in ok_codes:

			if user_message["message_text"] == f"Динамика курса за {x} дней":

				rates = []
				culc_rates = []

				for c_d in c_date:

					url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_d}"
					my_response = requests.get(url).json()
					cur_rate = my_response['Cur_OfficialRate'] 
					rates.append(cur_rate)


				for val in rates[:-1]:
					culc_rates.append(val - rates[rates.index(val) + 1])


				cur_message = f"Привет, динамика изменения {l_currency[1]} за {str(x)} дней:"

				for c_d, culc in zip(c_date, culc_rates):

					curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_d}"
					response = requests.get(curr_url)
					curr = response.json()
					date = (curr['Date'].replace("T00:00:00", ""))

					cur_message += f"\n {date}: {culc} "

				return cur_message

			if user_message["message_text"] == f"Курс {currency} на сегодня":

				date = user_message["current_date"]
				url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={date}"
				response = requests.get(url)
				username = user["username"]

				return f"Здравствуй, {username}, курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

			if user_message["message_text"] == f"Курс {currency} на {c_date}":

				date = c_date[0]
				url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={date}"
				response = requests.get(url)
				username = user["username"]

				return f"Здравствуй, {username}, курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

			if user_message["message_text"] == f"Курс валют {l_currency} на сегодня":

				date = c_date[0]
				username = user["username"]
				message = f"Здравствуй, {username}, курс запрошенных валют на {date} составляет"

				for l_c in l_currency:

					c = currency[l_c]
					url = f"https://www.nbrb.by/api/exrates/rates/{c}?ondate={date}"
					response = requests.get(url)
					message += f"\n за {response.json()['Cur_Scale']} {response.json()['Cur_Name']}: {response.json()['Cur_OfficialRate']} белорусских рублей "

				return message
		else:
			return f"Соедининение не удалось, мы получили ответ {status}"		
	else:
		return "Я не знаю такую страну"		



for u_ms in user_messages:
	print(m_bank(user, u_ms))
