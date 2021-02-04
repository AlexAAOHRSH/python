username = "Алексей"
city = "Брест"
date = "05.11.2020 "
weather = "холодная"



weather_message = ("Доброго времени суток {},сегодня {} в вашем прекрасном городе {} {} погода").format(username, date, city, weather)


print(weather_message)





currency_name_USD = "USD"
currency_scale_USD_BLN = 1
currency_rate_BLN = 2.52
currency_name_BLN = "BLN"

currency_name_RUB = "RUB"
currency_scale_RUB_BLN = 100.0
currency_rate_RUB = 3.1267

currency_name_UAH = "UAH"
currency_scale_UAH_BLN = 100.0
currency_rate_UAH = 9.28



message_currency_USD = ("На сегодня {} стоимость 1 {} {} {}").format(date, currency_name_USD, currency_rate_BLN, currency_name_BLN)
message_currency_RUB = ("Так же за 1 {} вы получите {} {}").format(currency_name_RUB, (currency_rate_RUB/currency_scale_RUB_BLN), currency_name_BLN )
message_currency_UAH = ("А за 1 {} вы получите {} {}").format(currency_name_UAH, (currency_rate_UAH/currency_scale_UAH_BLN), currency_name_BLN)

message_currency = [
message_currency_USD,
message_currency_RUB,
message_currency_UAH	
]

##print(message_currency_USD)
##print(message_currency_RUB)
##print(message_currency_UAH)

print(message_currency)
