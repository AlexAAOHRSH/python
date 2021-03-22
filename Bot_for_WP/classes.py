import requests
from settings import *
from time import sleep
from datetime import datetime, timedelta

def get_dates():
    date_format = '%Y.%m.%d'
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    after_tomorrow = today + timedelta(days=2)
    yesterday = today - timedelta(days=1)
    before_yesterday = today - timedelta(days=2)

    return {'today': today.strftime(date_format),
            'tomorrow': tomorrow.strftime(date_format),
            'after_tomorrow': after_tomorrow.strftime(date_format),
            'yesterday': yesterday.strftime(date_format),
            'before_yesterday': before_yesterday.strftime(date_format)}

class testing():

	def  test(self, text):
		self.send_message(self.get_updates()["chat_id"], "Братанчик, ты можешь выбрать уровень сложности:\n Лёгкий \n Средний \n Высокий")
		text = self.waiting(text, "тест python")
		counter = 0
		if text.lower() in ("легкий", "лёгкий"):
			self.send_message(self.get_updates()["chat_id"], "Ты выбрал легкий уровень сложности")
			self.send_message(self.get_updates()["chat_id"], "Поехали")

			for ez in ez_q:

				for l in range(len(ez)):

					self.send_message(self.get_updates()["chat_id"], f'{ez[l]["question"]} a. {ez[l]["answers"]["a"]} b. {ez[l]["answers"]["b"]} c. {ez[l]["answers"]["c"]} d. {ez[l]["answers"]["d"]}')
					last_text = self.last_message()
					text = self.waiting(text, "легкий", "лёгкий", last_text)
					if text.lower() == ez[l]["correct_answer"]:
						counter += 1

			self.send_message(self.get_updates()["chat_id"],f"Ты правильно ответил на {counter} вопросов из 11 ({(counter/11)*100}%)")

		if text.lower() == "средний":
			self.send_message(self.get_updates()["chat_id"], "Ты выбрал средний уровень сложности")
			self.send_message(self.get_updates()["chat_id"], "Поехали")

			for med in med_q:

				for l in range(len(med)):

					self.send_message(self.get_updates()["chat_id"], f'{med[l]["question"]} a. {med[l]["answers"]["a"]} b. {med[l]["answers"]["b"]} c. {med[l]["answers"]["c"]} d. {med[l]["answers"]["d"]}')
					last_text = self.last_message()
					text = self.waiting(text, "cредний", last_text)
					if text.lower() == med[l]["correct_answer"]:
						counter += 1

			self.send_message(self.get_updates()["chat_id"],f"Ты правильно ответил на {counter} вопросов из 6 ({(counter/6)*100}%)")

		if text.lower() == 'высокий':
			self.send_message(self.get_updates()["chat_id"], "Ты выбрал высокий уровень сложности")
			self.send_message(self.get_updates()["chat_id"], "Поехали")

			for hard in hard_q:

				for l in range(len(hard)):

					self.send_message(self.get_updates()["chat_id"], f'{hard[l]["question"]} a. {hard[l]["answers"]["a"]} b. {hard[l]["answers"]["b"]} c. {hard[l]["answers"]["c"]} d. {hard[l]["answers"]["d"]}')
					last_text = self.last_message()
					text = self.waiting(text, "высокий", last_text)
					if text.lower() == hard[l]["correct_answer"]:
						counter += 1

			self.send_message(self.get_updates()["chat_id"],f"Ты правильно ответил на {counter} вопросов из 6 ({(counter/6)*100}%)")

		# if text.lower() == 'кошмар':
		# 	send_message(get_updates()["chat_id"], "Больной ублюдок! Ладно ... ты сам на это пошёл..")

		return None




class courses():

	name_currency = ["EUR", "USD", "RUB"]

	currency = {"EUR": 292, "USD": 145, "RUB": 298}

	def ex_rates(self, text):

		self.send_message(self.get_updates()["chat_id"], "Учти, что я работаю только с EUR (евро), USD (доллар) и RUB (российский рубль)")
		self.send_message(self.get_updates()["chat_id"], "В данный момент ты можешь:\n Спросить курс валюты на сегодня  (используй конструкцию 'курс usd на сегодня').\
		\n Спросить курс валют на вчера (используй конструкцию 'курс usd на вчера').\n Спросить курсы валют на сегодня ('курсы валют на сегодня')")
		while text.lower() == 'курсы валют':
			text = self.last_message()
			sleep(3)
			if "курс" and "на сегодня" in text.lower():
				date = get_dates()['today']

				if "usd" in text.lower():
					url = f'{curr_url_1}{currency["USD"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} BYN")
				
				elif "eur" in text.lower():
					url = f'{curr_url_1}{currency["EUR"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} BYN")

				elif "rub" in text.lower():

					url = f'{curr_url_1}{currency["RUB"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс на {date} составляет {response.json()['Cur_OfficialRate']} BYN за {response.json()['Cur_Scale']}  {response.json()['Cur_Name']} ")
			if "курс" and "на вчера" in text.lower():
				date = get_dates()['yesterday']

				if "usd" in text.lower():
					url = f'{curr_url_1}{currency["USD"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} BYN")
				elif "eur" in text.lower():
					url = f'{curr_url_1}{currency["EUR"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс {response.json()['Cur_Name']} на {date} составляет {response.json()['Cur_OfficialRate']} BYN")

				elif "rub" in text.lower():

					url = f'{curr_url_1}{currency["RUB"]}{ondate}{date}'
					response = requests.get(url)

					self.send_message(self.get_updates()["chat_id"], f"Курс на {date} составляет {response.json()['Cur_OfficialRate']} BYN за {response.json()['Cur_Scale']}  {response.json()['Cur_Name']} ")
			if text.lower() == "курсы валют на сегодня":
				date = get_dates()['today']
				message_for_curses = f"Курс валют на {date}:"
				for n_c in self.name_currency:
					c = self.currency[n_c]
					url = f"https://www.nbrb.by/api/exrates/rates/{c}?ondate={date}"
					response = requests.get(url)
					message_for_curses += f"\n за {response.json()['Cur_Scale']} {response.json()['Cur_Name']}: {response.json()['Cur_OfficialRate']} белорусских рублей "

				self.send_message(self.get_updates()["chat_id"], message_for_curses)




class tel_bot(courses, testing):


	def __init__(self, token, bot_name):
		self.token = token
		self.bot_name = bot_name

	def init_url(self):

		url = f"https://api.telegram.org/bot{self.token}/"
		url_updates = f'{url}GetUpdates'
		url_send = f'{url}SendMessage'

		return {"url_updates": url_updates, "url_send": url_send}


	def get_updates(self):
		try:
			response = requests.get(self.init_url()["url_updates"])
			status_code=response.status_code
			if status_code in ok_codes:
				r = requests.get(self.init_url()["url_updates"]).json()

				r_updates =  r["result"][-1]["message"]

				last_user_text = r_updates['text']

				last_update_id = r_updates["message_id"]

				first_name = r_updates['from']['first_name']

				last_name = r_updates['from']['last_name']

				chat_id = r_updates['chat']['id']

				user = f'{first_name} {last_name}'

				return {"last_user_text": last_user_text, "last_update_id": last_update_id, "chat_id": chat_id, "user": user}
			else:
				print(f"Updates was not get successful. Status {status_code}")

				return {"ok" : False, "error_message" : f"Response code: {status_code}"}
		except Exception as e:
			raise Exception(f"Request was failed: {e}")

	def last_message(self):
		try:
			response = requests.get(self.init_url()["url_updates"])
			status_code=response.status_code
			if status_code in ok_codes:

				r = requests.get(self.init_url()["url_updates"]).json()
				r_updates =  r["result"][-1]["message"]
				last_user_text = r_updates['text']

				return last_user_text
			else:
				print(f"Updates was not get successful. Status {status_code}")

				return {"ok" : False, "error_message" : f"Response code: {status_code}"}
		except Exception as e:
			raise Exception(f"Request was failed: {e}")

	def send_message(self, chat_id, text):
		data={'chat_id': chat_id, 'text': text}
		try:
			res = requests.post(self.init_url()["url_send"], data)
			if res.status_code in ok_codes:
				print(f"Message was sent successful with status {res.status_code}")
			else:
				print(f"Message was not sent with status {res.status_code}")

		except Exception as e:
			raise Exception(f"Request was failed: {e}")

	def waiting(self, text, *waiting_text):
		while text.lower() in waiting_text:
			text = self.last_message()

		return text

	def help(self):
		text = "В данный момент ты можешь сделать следующее:\n Остановать меня (используй команду стоп).\n Поинтерисоваться курсами валют (напиши курсы валют).\
		\n Пройти тест по Питону (тест python)."
		self.send_message(self.get_updates()["chat_id"], text)



	def hello(self, text):
		if text.lower()	in ("привет", "hello", "привет!", "куку", "hello!", "здравствуй", "здравствуй!"):
			sleep(1)
			self.send_message(self.get_updates()["chat_id"], f"Здравствуй, {self.get_updates()['user']}.\n Напиши 'help' либо 'помощь'")
		elif text.lower() in ("спасибо","спасибо!","спс","спс!","благодарю!","благодарю"):
			sleep(1)
			self.send_message(self.get_updates()["chat_id"], "На здоровье!")
		elif text.lower() in ("жыве беларусь!", "жыве беларусь"):
			sleep(1)
			self.send_message(self.get_updates()["chat_id"], "Жыве!")
		# else:
		# 	sleep(1)
		# 	send_message(get_updates()["chat_id"], "Я не понимаю о чём ты!")

	def polling(self):
		message_id = 0

		while True:

			chat_id = self.get_updates()['chat_id']
			text = self.get_updates()['last_user_text']
			last_messsage_id = self.get_updates()['last_update_id']

			if last_messsage_id > message_id:

				if text.lower() in ("help", "помощь", "что ты умеешь?"):
					self.help()

				if text.lower() == 'курсы валют':
					self.ex_rates(text)

				if text.lower() == 'тест python':
					self.test(text)

				if text.lower() == 'стоп':
					sleep(1)
					self.send_message(chat_id,'Пока-пока!')
					break 

				self.hello(text)

				# send_message(chat_id, text)

				message_id = last_messsage_id



