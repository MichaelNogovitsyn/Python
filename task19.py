""" Дана последовательность из N целых чисел и число К.
Необходимо сдвинуть всю последовательность(сдвиг циклический) на К 
элементов вправо, К - положительное число.  """

nums=[1,2,3,4,5,6,7]
k=3
new_nums=[]
""" for i in range(k,len(nums)):
    new_nums.append(nums[i])
print(new_nums)
for j in range(0,k):
    new_nums.append(nums[j])
print(new_nums) """

print(nums[-k-1:]+nums[:k])