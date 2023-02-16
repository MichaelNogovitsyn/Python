""" Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. 
Ввод: 7 2 5
Вывод: 7 9 11 13 15 """

a = int(input("Enter a: "))
d = int(input("Enter d: "))
n = int(input("Enter n: "))
list_p=list()

def Progression(list1):
    list_1=list()
    for i in range(1,n+1):
        res = a + (i-1) * d
        list_1.append(res)
    return list_1

print(Progression(list_p))