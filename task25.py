""" # Напишите программу которая принимает на вход строку и отслеживает сколько 
раз каждый символ уже встречался. Количество повторов добовляется к символам 
с помощью постфикса формата _n """

print('Enter letters')
string = input().split(' ')
result = dict()

for char in string:
    if char in result:
        print(f'{char}_{result[char]}',end=' ')
        
    else:
        print(char,end=' ')
    result[char]=result.get(char,0)+1