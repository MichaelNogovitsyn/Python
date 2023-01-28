""" Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k
долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Примеры:
Примечание: каждое считывание производится с новой строки
3 2 4 -> yes
3 2 1 -> no """

numSlices = int(input('Enter quantity of slices: '))
n = int(input('Enter measure n: '))
m = int(input('Enter measure m: '))

def isBreakable(numS,n,m):
    if n>=2 and m>=2:
        if (numS<=n) or (numS<=m):
            return True
    else:
        return False
print('Yes' if (isBreakable(numSlices,n,m))  else 'No')

