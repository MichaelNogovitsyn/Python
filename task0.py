""" Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
 """

a = int(input("Enter a: "))
b = int(input("Enter b: "))

def sum(a,b):
    if b == 0:
        return a
    return 1+sum(a,b-1)

print(sum(a,b))