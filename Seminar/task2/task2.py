# Найдите сумму цифр трехзначного числа.

n=int(input('Введите 3х-значное число: '))

def SumDigit(n):
    num3=n%10
    num2=n//10%10
    num1=n//100
    sum=num1+num2+num3
    return sum

print("Сумма чисел = ",SumDigit(n))