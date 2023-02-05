""" Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

5
1 2 3 4 5
6
-> 5 """

from random import randint

n = int(input("enter size of array: "))
x = int(input("enter digit from 0 to 10: "))
a = [0]*n
res = 0
difference = 1000

for i in range(n):
    a[i] = randint(0, 10)
print(a)

for i in range(n):
    if abs(a[i]-x) < difference:
        difference = abs(x-a[i])
        res = a[i]
print("close to ", res)
