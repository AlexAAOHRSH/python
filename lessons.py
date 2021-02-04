import requests

val_cur = ["usd", "rub"]

ok_codes = (200, 201, 202)

cur_message = "Добрый день! Курсы валют на сегодня:"

for val in val_cur:
	curr_url = f"https://www.nbrb.by/api/exrates/rates/{val}?parammode=2"
	response = requests.get(curr_url)
	status = response.status_code 

	if status in ok_codes:
		currency = response.json()
		cur_name = currency['Cur_Name']
		cur_scale = currency['Cur_Scale']
		cur_rate = currency['Cur_OfficialRate']
		cur_message += f"\n {cur_rate} белорусских рублей за {cur_scale} {cur_name}."

	else:
		print(f"Соедининение не удалось, мы получили ответ {status}")


print(cur_message)
