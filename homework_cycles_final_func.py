###Та же лаба с циклами и курсами валют, только через функции

import requests

val_cur = "usd"

cur_id = 145

ok_codes = (200, 201, 202)

cur_date = ["24","25","26", "27", "28", "29", "30"]

rates = []

culc_rates = []

def curses():

	for c_date in cur_date:
		curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate=2020-11-{c_date}"
		response = requests.get(curr_url)
		status = response.status_code

		if status in ok_codes:
			currency = response.json()
			cur_rate = currency['Cur_OfficialRate'] 
			rates.append(cur_rate)
		else:
			print(f"Соедининение не удалось, мы получили ответ {status}")

	return  

print(rates)

for val in rates:
	culc_rates.append(val - rates[rates.index(val) + 1])

print(culc_rates)

cur_message = "Привет, динамика изменения доллара за последние дни:"

for c_date, culc in zip(cur_date, culc_rates):
	curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate=2020-11-{c_date}"
	response = requests.get(curr_url)
	status = response.status_code 

	if status in ok_codes:
		currency = response.json()
		date = (currency['Date'])
		###date.split('T') и date.replace('T00:00:00', '') почему-то не робит
		cur_message += f"\n {date}: {culc} "

	else:
		print(f"Соедининение не удалось, мы получили ответ {status}")

print(cur_message)

