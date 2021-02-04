"""
Даны два массива A и B. Удалить из массива А все четные элементы, стоящие на нечетных местах,
а из массива B элементы, у которых индекс совпадает с индеском удаленных элементов в массиве A
"""
from random import randint
"""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

counter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in A:
	for x in counter:
		if x % 2 != 0:
			if i % 2 == 0:
				A.remove(i)
				print(A)   
"""

 
A = [randint(0,50) for _ in range(10)]
B = [randint(0,50) for _ in range(10)]
print(A)
print(B)
for i in range(len(A))[::-1]:
    if i % 2 and not A[i] % 2:
        del A[i]
        del B[i]
print(A)
print(B)




