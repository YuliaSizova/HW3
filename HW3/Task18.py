# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# # *Пример:*

# # 5
# #     1 2 3 4 5
# #     6
# #     -> 5

import random
num_n=int(input('Введите число N: '))
massiv=[random.randint(1,10)for _ in range(num_n)]
print(massiv)
item=int(input('Введите  любое число: '))
c=abs(massiv[0]-item)
p=massiv[0]
for i in range(len(massiv)):
    if abs(massiv[i]-item)<c:
        c=abs(massiv[i]-item)
        p=massiv[i]

print(p)
