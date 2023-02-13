""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

4 -> 1 2 3 4
9 """
max = 0
sum = 0
n = int(input("Enter count of bush:"))
bushes = n * [0]

for i in range(n):
    bushes[i] = int(input(f"Enter berry count in {i+1} bush: "))

for i in range(len(bushes)):
    sum = bushes[i-2] + bushes[i-1] + bushes[i]
    if sum > max:
        max = sum
""" for i in range(3):
    sum = bushes[i-2] + bushes[i-1] + bushes[i]
    if sum > max:
        max = sum """
print(max)