file = open('text.txt', 'r',encoding='utf-8')
#print(file.readlines())
list_1 = list()
resultData=list()
for line in file.readlines():
    #print(line.split('\n')[0].split(';'))
    resultData.append(tuple(line.split('\n')[0].split(';')))
file.close()
print(resultData)