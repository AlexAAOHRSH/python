import telebot
import requests
import config
import json
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])

def welcome(message): 
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный, чтобы проверить твои знания в этом языке!\nХочешь меня опробовать?".format(message.from_user, bot.get_me()))
 
@bot.message_handler(content_types=['text'])

def first_stage(message):

	if message.text.lower() == 'да':
		bot.send_message(message.chat.id, f"Отлично! Я буду задавать тебе вопрос, на который будет только один правильный ответ, ты готов?")
		if message.text.lower() == 'да':
			bot.register_next_step_handler(message, second_stage)
	elif message.text.lower() == 'нет':
		bot.send_message(message.chat.id, "Возвращайся, когда будешь готов.")
	else:
		except message.text
		bot.send_message(message.chat.id, 'Я не понимаю, о чём ты😢. Ответь да или нет!')

options = (1,2,3,4)
answers = []

def second_stage(message):
	bot.send_message(message.chat.id, f"Замечательно, помчались!")
	bot.send_message(message.chat.id, f"И так, первый вопрос:\nВыберите верное написание для обозначения значения НИЧЕГО:\n1)None\n2)Nil\n3)none\n4)Null")
	for i in options:
		if str(i) == message.text:
			answers.append(i)
			bot.send_message(message.chat.id, f"{answers}")
	
# RUN
bot.polling(none_stop=True)