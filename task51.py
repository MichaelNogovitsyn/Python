values = [3,-2,3,3,3]


def same_by(characteristic, objects):
    result = True
    characteristic_list = [characteristic(x) for x in objects]
    for i in range(len(characteristic_list)-1):
        print(characteristic_list[i])
        if characteristic_list[i] != characteristic_list[i+1]:
            result = False
    return result

if same_by(lambda x: x>0, values):
    print('same')
else:
    print('different')
