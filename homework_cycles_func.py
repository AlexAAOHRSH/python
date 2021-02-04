import requests

val_cur = "usd"

cur_id = 145

ok_codes = (200, 201, 202)

cur_date = ["24","25","26", "27", "28", "29", "30"]

cur_message = "Привет, динамика изменения доллара за последние дни:"

rates = []

culc_rates = []

def curses(x):

	for c_date in cur_date:
		curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate=2020-11-{c_date}"
		response = requests.get(curr_url)
		status = response.status_code

		if status in ok_codes:
			currency = response.json()
			cur_rate = currency['Cur_OfficialRate'] 
			x.append(cur_rate)
		else:
			print(f"Соедининение не удалось, мы получили ответ {status}")

	return  x

def culc(x, y):

	for val in y:
		x.append(val - y[y.index(val) + 1])

	return x

def message(x):
	for c_date, culc in zip(cur_date, culc_rates):
		curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate=2020-11-{c_date}"
		response = requests.get(curr_url)
		status = response.status_code 

		if status in ok_codes:
			currency = response.json()
			date = (currency['Date'])
			###date.split('T') и date.replace('T00:00:00', '') почему-то не робит
			x += f"\n {date}: {culc} "

		else:
			print(f"Соедининение не удалось, мы получили ответ {status}")

	return x

curses(rates)
culc(culc_rates, rates)
message(cur_message)

print(cur_message)

	