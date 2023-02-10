""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
 """

a = int(input("Enter A: "))
b = int(input("Enter B: "))

def degree(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    return a*degree(a,b-1)
   
print(degree(a,b))