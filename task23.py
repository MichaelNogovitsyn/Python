""" # Данн массив, состоящий из целых чисел.
Напишите программу которая подсчтитает кол-во элементов массива,
больших предыдущего. """

arr=[0,-1,5,2,3,8,0,14,4,7]
count=0
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        count+=1
print(count)