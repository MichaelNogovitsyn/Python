
file = open('text.txt','r', encoding='utf-8')
data = ''.join(file.readlines())
print(data)
file.close