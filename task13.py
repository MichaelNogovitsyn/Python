n=int(input('enter count of watermelon: '))

arr=[i for i in range(n)]
for i in range(n):
    arr[i]=int(input('enter weight: '))

min=1
max=10
for i in range(n):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]
print(f'min={min} max = {max}')