import telebot
import requests
import ER_func as fl

c_date = ["2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04", "2020-12-05", "2020-12-06", "2020-12-07", "2020-12-08", "2020-12-09", "2020-12-10" ,"2020-12-11", "2020-12-12"]

currency = {"EUR": 292, "USD": 145, "RUB": 298}

l_currency = ["EUR", "USD", "RUB"]

cur_id = currency["USD"]
curr_url = f"https://www.nbrb.by/api/exrates/rates/{cur_id}?ondate={c_date}"

x = 12

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

bot = telebot.TeleBot('1445597949:AAFEmRr6f44zpsix8--OJeFhOdM2GhUQvwg')
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start. Теперь ты можешь попросить меня скинуть: \nКурс валюты на сегодня. \nКурс валюты на вчера. \nКурсы валют на сегодня. \nО чем ты меня попросишь?')

@bot.message_handler(content_types=['text'])

def send_text(message):
    # if message.text.lower() == 'динамика курса за n дней':
    #     m_bank_message = fl.m_bank(user, user_message1)
    #     bot.send_message(message.chat.id, m_bank_message)
    if message.text.lower() == 'курс валюты на сегодня':
        bot.send_message(message.chat.id, fl.m_bank(user, user_message2))
    elif message.text.lower() == 'курс валюты на вчера':
        bot.send_message(message.chat.id, fl.m_bank(user, user_message3))
    elif message.text.lower() == 'курсы валют на сегодня':
        bot.send_message(message.chat.id, fl.m_bank(user, user_message4))
    elif message.text.lower() == 'я люблю лёшу':
    	bot.send_message(message.chat.id, 'Лёша тоже тебя любит')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, чего ты хочешь')

bot.polling()