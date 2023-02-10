""" Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes  """

def is_simple_number(n):
    if n<2:
        return "No"
    for i in range(2,n):
        if n%i==0:
            return "No"
    return "Yes"

n= abs(int(input("Enter n: ")))

print(is_simple_number(n))