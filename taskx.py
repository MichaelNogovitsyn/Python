""" Даны два массива чисел. Требуется вывести те элементы первого 
массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит  число N - количество 
элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. 
Затем элементы второго массива
 """

n = int(input('Введите число n: '))
list1 = list(map(int,input().split()))

m = int(input('Введите число m: '))
list2 = list(map(int,input().split()))

""" for i in range(n):
    flag =False
    for j in range(m):
        if list1[i]==list2[j]:
            flag=True
            break
    if not flag:
        print(list1[i],end=' ') """

s1 = set(list2)
for i in range(n):
    if list1[i] not in s1:
        print(list1[i],end=' ') 