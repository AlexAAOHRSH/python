"""
Проверим на валидность каждую песню в списке. Если какие-то поля отсутствуют, то добавлем его со значением None и,
после добавления, принтим сообщение "В элемент Х оосутствовали поля ИМЯ ПОЛЯ"¬    
"""
songs = [
		{"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"},
		{"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"},
		{"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False},
		{"artist":"Hozier", "name":"Take Me To Church", "band":True},
		{"artist":"Evanescence", "name":"Bring Me To Life", "long":3.55},
		{"long":3.47, "band":True, "album":"Fight club"},
		{}
		]

atributes=["name","artist", "long", "band", "album"]
 
if songs:
	for song in songs:
		if song:
			for atribut in atributes:
				if atribut not in song.keys():
					song[atribut]=None
					if ("name" in song.keys()) and song["name"]:
						print(f"У песни с названием \"{song['name']}\" отсутствуeт полe: {atribut}")
					elif "artist" in  song.keys() and song["artist"]:
						print(f"У песни исполнителя \"{song['artist']}\" отсутствует поле: {atribut}")
					else:
						print(f"У той самой песни, без названия и исполнителя, отсутствуeт поле: {atribut}")
		else:
			print("В списке песен пустой словарь, пожалуйста, проверьте заполнение")
else:
	print("Your songs list is empty")

"""                                                                                                                                    
 ###### 2¬                                                                                                                           
 Создать профиль юзера                                                           
 
 user = {"name":"",                                                                                                                     
         "my_songs": {}}                                                                                                                    

                                                                                                                                          
 Добавиь к своему профиилю пару "мои песни":{}.  И теперь напишите скрипт, который будет проходиться по списку песен и добавлять их в  user["my_songs"}  по принципу "имя группы":[имя_песни, имя_песни]¬
                                                                                                                                       
 В результате должно получиться что-то вроде¬                                                                                                
 {"name":"",¬
  "my_artists":[],¬       
  "my_songs": {"Aerosmith": ["I don't wanna miss a think", "Girls of summer:"]}¬ 
               "Sabaton": ["Shiroyama"]}}¬
"""




user_one={"name":"Alexey",
		"my_songs":{}}
print(user_one)
 	
songs=[{"artist":"Макс Корж", "name":"Тепло"},
		{"artist":"Макс Корж", "name":"Времена"},
		{"artist":"Nirvana", "name":"Smells like teen spirit"},
		{"artist":"Макс Корж","name":"Ноябрь"},
		{"artist":"Макс Корж","name":"Нет Никаких Правил"},
		{"artist":"Nirvana", "name":"Come as you are"},
		{"artist":"Linkin Park", "name":"In the end"},
		{"artist":"Linkin Park","name":"Numb"},
		{"artist":"Linkin Park", "name":"One More light"},
		{"artist":"Green Day", "name":"Boulevard of Broken Dreams"},
		{"artist":"Green Day", "name":"Wake Me Up, When September Ends"}
		]

for song in songs:
	if song["artist"] not in user_one["my_songs"].keys():
		if song["artist"]:
			print(f"Добавляем нового исполнителя \"{song['artist']}\" ")
			user_one["my_songs"][song["artist"]]=[song["name"]]
		else:
			print(f"Добавляем каталог для  песен с неизвестным или  без исполнителя")
			user_one["my_songs"][song["artist"]]=[song["name"]]
	else:
		print(f"\"{song['artist']}\" уже существует")
		if song["name"] not in user_one["my_songs"][song["artist"]]:
			user_one["my_songs"][song["artist"]].append(song["name"])
			user_one["my_songs"][song["artist"]]=sorted(user_one["my_songs"][song["artist"]])

		else:
			print(f"Песня \"{song['name']}\" уже есть в списке")

print(user_one)



"""                                        
#### 3¬
Придумать систему совпадения вкусов двух юзеров с заполненными данными  песнях¬                                                           
                                                                                                                                       
Сравнивать два пользовательских профиля и выводить совпадение их вкусов в процентах.¬                                                       
                                                                                                                                        
Для начала при равном колличестве песен и групп, в более сложном варианте - в произвольном. Т.е у одного пользователя список из трех песен одной группы а у друого 20 от 5 разных.
"""



user_two={"name":"Kesha",
			"my_songs":{"Макс Корж":["Времена", "2 Типа Людей", "Нет Никаких Правил"]}}

profile_one=user_one
profile_two=user_two
songs_count=0
same_songs=0


if profile_one:
	if profile_two:
		for singer in profile_one["my_songs"]:
			for song in (profile_one["my_songs"][singer]):
				songs_count+=1
				if singer in profile_two["my_songs"]:
					if song in profile_two["my_songs"][singer]:
						#print("есть такая песня")
						same_songs+=1
		print(f"Уровень совпадения вкуса у пользователя {profile_one['name']} с пользователем {profile_two['name']} составляет {(same_songs/songs_count)*100:.2f} процентов")

	else:
		print("Контрольный профиль пуст")	
else:
	print("Сравниваемый профиль пуст")