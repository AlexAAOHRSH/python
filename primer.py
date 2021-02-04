import datetime


stroka = "nu i eta dolzhna prokatit' s lubim chislom, k primery 867, pochemu net?"

str_int = ""



for i in stroka:

	try:

		int(i)

	except Exception:
		None

	else:

		str_int += i



print(str_int)


date_time_now = datetime.datetime.now()

str_date_time_now = str(date_time_now)

date_now = ""

for date in str_date_time_now[0:10]:
	date_now += date

print(date_now)

print(datetime.datetime.date(date_time_now))

dates = []

for date in range(24, 0):
	dates.append(date)

print(dates)
	
d = " "

print(len(d))