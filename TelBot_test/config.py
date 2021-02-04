import requests

token = '1564817798:AAHsKi8dsB9ETgnDNEGDdS-R-jdyTuOwDJo'
bot_name  = "Py_Th_On_Test_Bot"




def func(message, second):
	print(message)
	print(second)

func("Hi", "Hello")


# func("alloha")



requests.get("https://www.nbrb.by/api/exrates/rates/145?ondate=2020-12-01")

requests.get("https://www.nbrb.by/api/exrates/rates/145?ondate=2020-12-01", verify = False)
