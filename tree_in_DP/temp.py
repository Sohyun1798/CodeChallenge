root = 5
temp = {1: [3], 2: [3], 3: [], 4: [3], 5: [4, 6], 6: [7, 8], 7: [], 8: [], 9: [6]}

for key in range(1, 10):

    if key < root:
        if temp[key] == []:
            temp.pop(key)
        else:
            for ele in temp[key]:
                if ele > key:
                    if key not in temp[ele]:
                        temp[ele] += [key]
                
                    temp[key].remove(ele)
                    if temp[key] == []:
                        temp.pop(key)

    if key > root:
        if temp[key] == []:
            temp.pop(key)
        else:
            for ele in temp[key]:
                if ele < key:
                    if key not in temp[ele]:
                        temp[ele] += [key]

                    temp[key].remove(ele)
                    if temp[key] == []:
                        temp.pop(key)


print(temp)


   