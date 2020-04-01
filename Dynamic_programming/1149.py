def get_input():

    n = int(input())
    input_list = []

    for _ in range(n):
        input_list.append(list(map(int, input().split())))
    
    return n, input_list

def dp_1149():

    n, input_list = get_input()
    ans = []
    
    for i in range(1,n+1):
        ans.append([0 for _ in range(3)])

    for i in range(n):
        if i == 0:
            ans[0] = input_list[0]
        else:
            for k in range(3):
                if k == 0:
                    temp1 = ans[i-1][1]+input_list[i][k]
                    temp2 = ans[i-1][2]+input_list[i][k]
                    ans[i][0] = min(temp1, temp2)
                elif k == 1:
                    temp1 = ans[i-1][0]+input_list[i][k]
                    temp2 = ans[i-1][2]+input_list[i][k]
                    ans[i][1] = min(temp1, temp2)
                else:
                    temp1 = ans[i-1][0]+input_list[i][k]
                    temp2 = ans[i-1][1]+input_list[i][k]
                    ans[i][2] = min(temp1, temp2)

    return min(ans[n-1])

print(dp_1149())




