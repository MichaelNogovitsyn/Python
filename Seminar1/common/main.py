import math
print ("Введите км в день:")
n = int(input())
print ("Введите км маршрут:")
m = int(input())


def day(n,m):
    days = m/n
    return days

days = day(n,m)
print( math.ceil(days))