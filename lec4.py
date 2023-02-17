data = [1,2,3,5,8,15,23,38]

list_res = []

""" for i in list_set:
    if i%2==0:
        list_res.append((i,i*i))
print(list_res) """

def select(f,col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)] 

res = select(int,data)
#print(res)

res = where(lambda x: x%2==0,res)
print(res)

res=list(select(lambda x: (x,x**2),res))
##print(res)

d = [(i,i**2) for i in data if i%2==0]
#print(d)

""" list_1 = [x for x in range(1,20)]
print(list_1)
list_1=list(map(lambda x: x+10,list_1 ))
print(list_1) """

""" data =list(map(int,input('Enter data:').split(' ')))
print(data)  """

res = list(filter(lambda x: x%10==5, data))

print(res)