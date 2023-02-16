from random import randint

nums=[1,2,3,4,5,6,7,8,9,10]
unic=[1,2,3] 
for element in nums:
    if element not in unic:
        unic.append(element)       
print(len(set(nums)))

arr = input("Enter data".split(' '))
print('arr=',arr)

list2=[i for i in range(1,101) if i%2 !=0] 

arr =list(map(int,input('Enter data:').split(' ')))
print(arr)

print(nums[-k-1:]+nums[:k])

#####
d=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]

s=set()
for element in d:
    for value in element.values():
        s.add(value)
print(s)
##########

a=[0]*n

str1="апрлоравролаврлолдфво"
char = 'п'
if char in str1:
    print()

list1 = list(map(int,input().split()))

#####################################
file = open('text.txt', 'r',encoding='utf-8')
#print(file.readlines())
list_1 = list()
resultData=list()
for line in file.readlines():
    #print(line.split('\n')[0].split(';'))
    resultData.append(tuple(line.split('\n')[0].split(';')))
file.close()
print(resultData)
###################################################