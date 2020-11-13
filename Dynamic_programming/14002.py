def get_input():

    n = int(input())

    input_list = []
    input_list.extend(list(map(int, input().split())))
    
    return input_list

def dp_14002():

    input_list = get_input()
    temp = []

    for i in range(len(input_list)):

        if i == 0:
            temp.append(input_list[i])
            j = 0

        else:
            if temp[j] < input_list[i]:
                temp.append(input_list[i])
                j += 1

    ans = len(temp)

    return ans, temp

print(dp_14002())




