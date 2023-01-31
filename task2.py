# найти число фибоначчи по счету
n=int(input('Enter N: '))


def Fibonacci(n):
    index=2
    c=1
    res=1    
    while res<n:
        res=c+res
        c=res-c
        index+=1
        if c>n:
            index=0
        print(res)
    if index==0:
        return -1
    else: return index
print(Fibonacci(n))