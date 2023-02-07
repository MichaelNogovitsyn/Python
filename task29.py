n =int(input("Введите число: "))
max=-1
while n!=0:
    if max<n:
        max=n
    n=int(input("Введите число: "))    
print(max)