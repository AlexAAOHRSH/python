##### 1
"""
Напиште скрипт, убеждающийся, что элемент - это не пустой словаь.

Затем -  все ли необоходимые поля есть у элемента:

artist
name
long
band
album

Если поле отсутствует, добавить пару ключ-значение со значением None. Наприме нет элемента name
нужно добавить  "name":None
"""

element_one = {"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"}
element_two = {"artist":"Guns'n Roses", "name": "Patience", "band": True}

if type(element_one) == dict and type(element_two) == dict:
	print("elements is dict")
else:
    print("elements is not dict")	





if element_one == 0:
	print("element_one is empty")
else: 
    print("element_one is not empty")

if element_two == 0:
	print("element_two is empty")
else: 
    print("element_two is not empty")    




fields = ("artist", "name", "long", "band", "album")

for field in fields:
	if field in element_one:
		print(f"{field} in element_one")
	else:
		element_one.update([(field,None)])

for field in fields:
	if field in element_two:
		print(f"{field} in element_two")
	else:
		element_two.update([(field,None)])




##### 2

element = {"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"}


songs = [
		{"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"},
		{"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"},
		{"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None},
		]

"""
Напишем скрипт, который проверяет, есть ли элемент в списке и, если нет, добавляет его в конец.

- Убедимся, что наш спсок песен, это, собственно, не пустой список.
Если нет - сообщим об этом.
Если да - убедимся, что выбранный элемент не находиться в списке и вставим его в конец.

В результате должна быть последовательность уникальных элементов (можно преобразовать список в сет)
"""
print(songs)

if songs == 0:
	print("BAD")
elif element in songs:
	print("GOOD")
else:
	songs.append(element)

print(songs)

##### 3

"""
Объеденим предыдущие два пункта  - вставим проверку на наличие элементов из певого пункта в скрипт, 
выполняющий добавление элемента в список во второй

- Убеждаемся, что наш объект - непустой словарь
- Проверяем, что у него есть все необоходмые поля, а если нет - добавляем поле со значением None
- Добавим этот элемент в уникальную последовательность других песен.
"""
my_song = {"artist":"Hozier", "name": "Take Me To Church" ,"long": 4.02}
if type(my_song) == dict:
	print("good")
else:
	print("pisdec nahoy blyat")


for field in fields:
	if field in my_song:
		print(f"{field} in my_song")
	else:
		my_song.update([(field,None)])

songs.append(my_song)

print(songs)		