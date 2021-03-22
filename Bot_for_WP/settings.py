
token = '1387500601:AAG1aLzoOY1lv4sstK5yOcvN9aChnaXTMyM'

bot_name = "@test1904859205_bot"

url = f"https://api.telegram.org/bot{token}/"

ok_codes = (200, 201, 202)

name_currency = ["EUR", "USD", "RUB"]

currency = {"EUR": 292, "USD": 145, "RUB": 298}

curr_url_1 = "https://www.nbrb.by/api/exrates/rates/"

ondate = "?ondate="

basics_easy=[{"question":"\nВыберите верное написание для обозначения значения НИЧЕГО:\n",
			"answers":{ "a":"None\n",
						"b":"Null\n",
						"c":"none\n",
						"d":"nothing\n"},
			"correct_answer":"a"},

			{"question":"\nPython это компилируемый язык или интерпретируемый:\n",
			"answers":{ "a":"Компилируемый\n",
						"b":"Интерпретируемый\n",
						"c":"Ни один из вариантов неверен\n",
						"d":"Нивелируемый\n"},
			"correct_answer":"b"},

			{"question":"\nЧто выведет код: print('2'+'2')\n",
			"answers":{ "a":"\'4\'\n",
						"b":"4\n",
						"c":"вызовет Exception\n",
						"d":"\'22\'\n"},
			"correct_answer":"d"}
			]

basics_medium=[{"question":"\nМожно ли в Python  трансформировать значения одного типа в другой?\n",
				"answers":{	"a":"Можно, с некоторыми логическими ограничениями. Например, число может стать строкой, но None не станет списком\n",
							"b":"Можно без всяких лимитов - хоть строку превратить в целое число\n",
							"c":"Нет, трансформация типа невозможна\n",
							"d":"В Python  нет различных типов данных\n"},
				"correct_answer":"a"},

				{"question":"""\nЧто выведет следующий код:
for i in (0, 1, 2, 3):
	print(i)
	if i>=2:
		break\n""",
				"answers":{	"a":"в столбик: 0, 1\n",
							"b":"ничегоб скрипт отработает без вывода в командную строку\n",
							"c":"в столбик: 0, 1, 2, 3\n",
							"d":"в столбик: 0, 1, 2\n"},
				"correct_answer":"d"}
				]

basics_hard=[{"question":"\nВыберите, что из этого является неизменяемой структурой:\n",
				"answers":{	"a":"{“Some value”, None, 26}\n",
							"b":"frozenset({“Some value”, None, 26})\n",
							"c":"[“Some value”, None, 26]\n",
							"d":"{“Some value”: None, “size”: 26}\n"},
				"correct_answer":"b"},

			{"question":"\nВыберите, какой из вариантов содержит только неизменяемый структуры:\n",
			"answers":{	"a":"int, str, float, None, frozenset, tuple\n",
						"b":"int, str, float, None, frozenset, dict\n",
						"c":"dict, list, tuple, int\n",
						"d":"set, str, tuple, int\n"},
			"correct_answer":"a"},

			{"question":"\nГде допущена ошибка?\n",
			"answers":{	"a":"list(1,3,5,None, 'Egor')\n",
						"b":"frozenset({'name': 'My name', 'age': 45})\n",
						"c":"frozenset({'My name', 'age', 45})\n",
						"d":"8,15,6,23,42\n"},
			"correct_answer":"b"},

			{"question":"""\nЧто будет выведено в командной строке в результате выполнения кода:
b=5
a=(1, b, 4)
b=6
print(a)\n""",
			"answers":{	"a":"(1, b, 4)\n",
						"b":"(1, 6, 4)\n",
						"c":"Exception(т к tuple - неизменяемая структура)\n",
						"d":"(1, 5, 4)\n"},
			"correct_answer":"d"}
			]

func_easy=[{"question":"\nКлючевое слово при объявлении функции:\n",
			"answers":{	"a":"func\n",
						"b":"function\n",
						"c":"def\n",
						"d":"Нет никакого ключевого слова\n"},
			"correct_answer":"c"},

			{"question":"\nОбязательно ли ключевое слово return при объявлении функции?\n",
			"answers":{	"a":"Да\n",
						"b":"Нет\n",
						"c":"Зависит от условий - иногда да, иногда нет\n",
						"d":"Если функция утрируемая, то да, в остальных случаях - нет\n"},
			"correct_answer":"b"},

			{"question":"\nЧто возвращает функция, если не указано ключевое слово return?\n",
			"answers":{	"a":"Null\n",
						"b":"result\n",
						"c":"False\n",
						"d":"None\n"},
			"correct_answer":"d"}
			]

func_medium=[{"question":"""\nЧто мы получим в результате выполнения данного кода?
def somefunc():
    return True

if somefunc():
    print('Hello')
else:
    print('Bye!')\n""",

			"answers":{	"a":"Напечатается 'Bye!'\n",
						"b":"Получим исключение AssertError\n",
						"c":"Напечататься 'Hello!'\n",
						"d":"Ничего\n"},
			"correct_answer":"c"}
			]

func_hard=[{"question":"""\nКакой результат мы получим, исполнив код ниже?
def myfunc(i):
    return 10

i=42
n=myfunc()
print(n)\n""",

			"answers":{	"a":"Напечатается 42\n",
						"b":"Напечатается 10\n",
						"c":"Будет Exception\n",
						"d":"None\n"},
			"correct_answer":"c"}
			]

api_easy=[{"question":"\nТакое понятие как API:\n",
			"answers":{	"a":"Относиться только к работе с интернетом\n",
						"b":"Относиться только к работе с железом напрямую\n",
						"c":"Ни один из вариантов не верен\n",
						"d":"Это из области разработки видеоигр\n"},
			"correct_answer":"c"},

			{"question":"\nМожет ли быть API у операционной системы?\n",
			"answers":{	"a":"Да\n",
						"b":"Нет\n",
						"c":"Пойдем взорвем башню 'Арасаки', или хотя бы фургон поломаем!\n",
						"d":"Уже готов!\n"},
			"correct_answer":"a"},
		]

exception_easy=[{"question":"""\nЗапустив данный код:
try:
    int("Hello")
except Exception:
    print("Hello")

Мы получим:\n""",
				"answers":{	"a":"Ничего\n",
							"b":"В командной строке выведется 'Hello'\n",
							"c":"Exception: Hello\n",
							"d":"Довольно устрашающее сообщение о том, что жизнь кортка и полна страданий\n"},
				"correct_answer":"b"},
				]

exception_medium=[{"question":"\nЧто произойдет если вызывать код: raise Exception('Some exception')\n",
					"answers":{	"a":"Интерпретатор вызовет исключение и получим в консоли Exception: Some exception\n",
								"b":"Мы получм сообщение о том, что код написан неверно\n",
								"c":"Ничего\n",
								"d":"Получим сценарий комедийного хоррора про маньяка с Винсом Воном\n"},
					"correct_answer":"a"}
				]

protocol_easy=[{"question":"\nКакой из вариантов содержит исключительно упоминания протоколов?\n",
				"answers":{	"a":"Python, HTTPS, TCP/IP, MMS\n",
							"b":"TCP/IP, Megadeth, JavaScript, SMS\n",
							"c":"BitTorrent, HTTP, HTTPS, протокол медицинского осмотра\n",
							"d":"Все\n"},
				"correct_answer":"c"}
				]

protocol_hard=[{"question":"\nЕсли мы по протоколу HTTP посылаем на сервер запрос, что мы получим:\n",
				"answers":{	"a":"В любом случае получим response\n",
							"b":"В зависимости от настроек - можем получить строку, джсон или еще что-то\n",
							"c":"Либо response либо None\n",
							"d":"Та хрен его знает\n"},
				"correct_answer":"a"}
				]

import_easy=[{"question":"""\nУ нас есть папка folder с двумя файлами  file_one.py  и file_two.py
folder\\
    file_one.py  
    file_two.py
Если я хочу подключить из file_one.py в file_two.py все его содержимое, какой код мне использовать:\n""",

				"answers":{	"a":"from file_one import *\n",
							"b":"import all from  file_one\n",
							"c":"from file_one.py import *\n",
							"d":"import * from  file_one\n"},
				"correct_answer":"a"}
				]

import_medium=[{"question":"""\nУ нас есть папка со структурой:
folder\\
    main.py
    subfolder\\
        some_file.py
        sub_file.py
Если я хочу подключить файл sub_file.py в main.py, что именно мне следует прописать в файле main.py\n""",
				
				"answers":{	"a":"connect subfile.py to main.py\n",
							"b":"import subfolder.sub_file\n",
							"c":"import sub_file from subfolder\n",
							"d":"import sub_file.py from subfolder\n"},
				"correct_answer":"b"},

				{"question":"""\nfile_1.py и file_2.py находяться в одной папке.как следует
вызвать функцию some_func из file_1.py импортированную в file_2.py следующим образом:
import file_1 as sun\n""",
				
				"answers":{	"a":"sun.some_func()\n",
							"b":"some_func()\n",
							"c":"file_1.some_func\n",
							"d":"file_1.sun.some_func()\n"},
				"correct_answer":"a"}
				]


questions={ "basics":{ "easy":basics_easy,
						"medium": basics_medium,
						"hard": basics_hard},
			"function":{"easy":func_easy,
						"medium":func_medium,
						"hard":func_hard},
			"api":{"easy":api_easy},
			"protocol":{"easy":protocol_easy,
						"hard":protocol_hard},
			"import":{"easy":import_easy,
					"medium":import_medium},
			"exception":{"easy":exception_easy,
						"medium":exception_medium},
			"all":{}
			}


ez_q = []
med_q = []
hard_q = []
keys = []

for key in questions.keys():
	keys.append(key)


for k in keys:
	if 'easy' in questions[k].keys():
		ez_q.append(questions[k]['easy'])

for k in keys:
	if 'medium' in questions[k].keys():
		med_q.append(questions[k]['medium'])

for k in keys:
	if 'hard' in questions[k].keys():
		hard_q.append(questions[k]['hard'])


# print(ez_q)


