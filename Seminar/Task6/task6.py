""" Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, г
де сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета

Примеры:
385916 -> yes
123456 -> no """

ticketNum=int(input('Input ticket number: '))
def isHappy(ticket):
    n1=ticket//100000
    print(n1)
    n2=ticket//10000%10
    print(n2)
    n3=ticket//1000%10
    print(n3)
    n4=ticket//100%10
    print(n4)
    n5=ticket//10%10
    print(n5)
    n6=ticket%10
    print(n6)
    return (n1+n2+n3)==(n4+n5+n6)

print(isHappy(ticketNum))