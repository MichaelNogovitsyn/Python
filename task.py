n=int(input('Enter N: '))
i=1
result=1
while i < n:
    result+=result*i
    i+=1
print(result)