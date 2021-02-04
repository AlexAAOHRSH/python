"""
В одномерном целочисленном массиве вычислить:
	номер максимального элемента массива;
	сумму элементов массива расположенного после минимального элемента;
Преобразовать массив таким образом, чтобы в первой его половине располагались элементы, стощие в нечетных позициях,
а во второй половине - элементы, стоящие на четных позициях
"""


from random import randint

A = [randint(0,50) for _ in range(10)]

print(f"Numbers on list {A}")

print(f"Max number in list = {max(A)} ")
for maks in A:
	if maks == max(A):
		print(f"Index of max number in list = {A.index(maks)}")


print(f"Min number in list = {min(A)}")
summa = 0
min_id = A.index(min(A)) 
for i in range(min_id + 1, 9):
    summa += A[i]
print(f"Sum of number after minimal num = {summa}")

B = []
print(A)
print(B)
for x in A:
	if A.index(x) % 2 == 0:
		B.append(x)
			
print(A)
print(B)

for q in B:
	del A[A.index(q)]

print(A)

for w in B:
	A.append(w)

print(A)
