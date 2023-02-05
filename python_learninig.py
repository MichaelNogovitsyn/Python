nums=[1,2,3,4,5,6,7,8,9,10]
unic=[1,2,3] 
for element in nums:
    if element not in unic:
        unic.append(element)       
print(len(set(nums)))

arr = input("Enter data".split(' '))
print('arr=',arr)

list2=[i for i in range(1,101)] 

arr =list(map(int,input('Enter data:').split(' ')))
print(arr)

print(nums[-k-1:]+nums[:k])
