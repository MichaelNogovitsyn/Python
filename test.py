# Задача. I1.11. Известны год и номер месяца рождения человека, а также год и номер месяца сегодняшнего дня (январь — 1 и т. д.). 
# Определить возраст человека (число полных лет). В случае совпадения указанных номеров месяцев считать, что прошел полный год.
print('Enter year of born')
a=int(input())
print('Enter mounth of born')
b=int(input())
print('current year')
c=int(input())
print('Enter current mounth')
d=int(input())

def getAge(year, mounth, curYear, curMounth):
    if curMounth>=mounth:
        age=curYear-year
    else:
        age=curYear-year-1
    return age
    
print(getAge(a,b,c,d))