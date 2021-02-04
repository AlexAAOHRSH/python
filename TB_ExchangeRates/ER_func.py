import requests

l_currency = ["EUR", "USD", "RUB"]

currency = {"EUR": 292, "USD": 145, "RUB": 298}

cur_id = currency["USD"]

c_date = ["2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04", "2020-12-05", "2020-12-06", "2020-12-07", "2020-12-08", "2020-12-09", "2020-12-10" ,"2020-12-11", "2020-12-12"]

x = 11

ok_codes = (200, 201, 202)

user = {"username": "Алексей",
		"country": "BY"}

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

def m_bank(user, user_message):

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


			cur_message = f"Динамика изменения {l_currency[1]} за {str(x)} дней:"

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

			return f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

		if user_message["message_text"] == f"Курс {currency} на {c_date}":

			date = c_date[10]
			url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={date}"
			response = requests.get(url)
			username = user["username"]

			return f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} " 

		if user_message["message_text"] == f"Курс валют {l_currency} на сегодня":

			date = c_date[11]
			username = user["username"]
			message = f"Курс запрошенных валют на {date} составляет"

			for l_c in l_currency:

				c = currency[l_c]
				url = f"https://www.nbrb.by/api/exrates/rates/{c}?ondate={date}"
				response = requests.get(url)
				message += f"\n за {response.json()['Cur_Scale']} {response.json()['Cur_Name']}: {response.json()['Cur_OfficialRate']} белорусских рублей "

			return message
	else:
		return f"Соедининение не удалось, мы получили ответ {status}"		
	
