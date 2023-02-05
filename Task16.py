""" Задача 16: Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[0..N-1]. 
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел A[i]. 
Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1 """
from random import randint

n = int(input("enter size of array: "))
x = int(input("enter digit from 0 to 5: "))
a=[0]*n
count=0
for i in range(n):
    a[i]=randint(0,5)
print(a)

for i in range(n):
    if x==a[i]: count+=1
print(x,"times")