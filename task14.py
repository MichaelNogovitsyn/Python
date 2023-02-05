""" Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2^k), не превосходящие числа N.
10 -> 1 2 4 8 """

N = int(input('Enter N: '))

res=0
k=0
while res <= N:
    res=pow(2,k)
    k+=1
    if res>N:
        break
    print(res,end=', ')