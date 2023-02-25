from random import randint

nums=[1,2,3,4,5,6,7,8,9,10]
unic=[1,2,3] 
for element in nums:
    if element not in unic:
        unic.append(element)       
print(len(set(nums)))
print(''.join(f'{e:<4}' for e in rows_list))
##############     List   ####################
arr = input("Enter data".split(' '))
print('arr=',arr)

a=[0]*5
list2=[i for i in range(1,101) if i%2 !=0] 
d = [(i,i**2) for i in data if i%2==0]

################   Dictionares  Set    #################
d=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]

s=set()
for element in d:
    for value in element.values():
        s.add(value)
print(s)

#################### Lambda #####################
lambda x: x%2==0
lambda x: (x,x**2)
#################### Map  Filter Zip  #####################
list_1 = [x for x in range(1,20)]
print(list_1)
list_1=list(map(lambda x: x+10,list_1 ))

arr =list(map(int,input('Enter data:').split(' ')))
list1 = list(map(int,input().split()))

res = list(filter(lambda x: x%10==5, data))
##################     File    ###################
file = open('text.txt', 'r',encoding='utf-8')
#print(file.readlines())
list_1 = list()
resultData=list()
for line in file.readlines():
    #print(line.split('\n')[0].split(';'))
    resultData.append(tuple(line.split('\n')[0].split(';')))
file.close()
print(resultData)

with open('text.txt','r', encoding='utf-8') as file:
    data = ''.join(file.readlines())
    print(data)


###################################################