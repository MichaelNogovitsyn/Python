
from random import randint
right=100000000
left=0

array=[1,3,5,8,11,55,66,100]

array2=[555,22,3,1,44,2,33,6,55,100]

x=randint(left,right)


count_bin=1
mid=(right + left) // 2


while x!=mid:
    print(mid)
    if x<mid: 
        print("больше")
        right=mid-1
    else: 
        print("меньше")
        left=mid+1
    mid=(right + left) // 2
   # y=int(input('Р’РІРµРґРё С‡РёСЃР»Рѕ'))
    count_bin+=1
print(count_bin)

