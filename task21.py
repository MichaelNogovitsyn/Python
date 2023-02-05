#Напишите программу для печати всех уникальных значений в словаре

d=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]

s=set()
for element in d:
    for value in element.values():
        s.add(value)
print(s)