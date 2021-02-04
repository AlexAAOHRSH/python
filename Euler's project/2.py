a = 1

b = 2

summa = 0

for i in range(4000000):
	if i == (a + b):
		a == b 
		b += a

		if i % 2 == 0:
			summa += i

print(summa)