#Дан список чисел. Определите сколько в нем встречаются различных чисел
nums= [1,1,2,0,-1,2,3,4,4,6,4]
""" unic=[]

for element in nums:
    if element not in unic:
        unic.append(element)       
print(len(unic)) """

print(len(set(nums)))

arr =list(map(int,input('Enter data:').split(' ')))
print(arr)