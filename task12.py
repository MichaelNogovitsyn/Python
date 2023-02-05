""" Задача 12: Петя и Катя – брат и сестра. 
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а 
Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3 """


#Дано:
S=int(input('Введите сумму чисел S: '))
P=int(input('Введите произведение чисел P: '))
#Решим квадратное уравнение
#X^2-Sx+P=0
#D=S^2-4P
D=pow(S,2)-4*P
x=(S+pow(D,0.5))/2
y=S-x
print(f'x={x} y={y}')
