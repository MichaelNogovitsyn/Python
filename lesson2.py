list1=[1,3,5]
print(*list1)
list1.append(9)
list1.append(11)
print(*list1)

list1.pop()
print(*list1)
list1.pop(0)
print(*list1)

list2=[i for i in range(1,101)]
print(list2)
list3=[i for i in range(1,101) if i%2==0]
print(list3)