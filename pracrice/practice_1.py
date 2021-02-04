import requests

curr = "EUR"
curr_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={curr}&json"

###bel_bank = "https://www.nbrb.by/api/exrates/rates/usd?parammode=2"

ukr_bank = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&json"


response = requests.get(curr_url)



currency = response.json()

date = currency[0]['exchangedate']
curr_name1 = currency[0]['txt']
rate = currency[0]['rate']
###curr_name2 = currency[0]['cc']



###print(message)

val_list = ["RUB", "EUR", "USD"]
for val in val_list:
	curr_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&json"
	response = requests.get(curr_url)
	currency = response.json()
	date = currency[0]['exchangedate']
	curr_name1 = currency[0]['txt']
	rate = currency[0]['rate']
	###curr_name2 = currency[0]['cc']
	message = f"За 1 {curr_name1} на {date} число получишь {rate} UAH "
	print(message)




"""
Задача - написать скрипт, который будет брать набор аббревиатур валют и возвращать текст сообщения для пользователя, где будет расписана информация по заданным валютам.

- извлечем данные по курсу валюты на сегодня
- создадим шаблон сообщения, в которое будет подставляться информация о курсе
- сделаем так, чтобы мы задавали последовательность валютных аббревиатур и наш скрит извлекал информацию окурсе каждой из них и все это комбинировал в одно сообщение 




- что делать, если заданной валюты нет и ответ приходит не такой, как мы ожидали?
- проблемы с интернетом/доступом?
(200, 201)



Усложним скрипт - сделаем так, чтобы мы имели данные о юзере и данные о сообщении в виде двух словарей.
- Создадим профиль юзерв в виде словаря, с полями 
username: str  
country: str

- создадим словарь message с полями user_id  и message_text где user_id это переменная user а message_text - набор и з аббревитур валют.


Затем, используя словарь message мы извлекаем из него зачение country, на его основе выбираем, тащить данные с беларуского апи или украинского

И выводим сообщение, куда добавлены имя пользователя и данные о курсе валют
"""