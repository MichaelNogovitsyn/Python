""" Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 
Вывод:
2
 """


list_n = list(map(int, input().split())) 
count=0
for i in range(len(list_n)-1):
    if list_n[i] is None:
        continue
    count_i=1
    flag = True
    for j in range(i+1,len(list_n)):

        if list_n[j] is not None and list_n[i]==list_n[j]:
            count_i+=1
            list_n[j]=None
    count+=count_i//2
    print(count,count_i)
print(count)    
