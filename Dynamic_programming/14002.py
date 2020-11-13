def get_input():

    n = int(input())

    input_list = []
    input_list.extend(list(map(int, input().split())))
    
    return n, input_list

def dp_14002():

    n, input_list = get_input()

    ans = [0 for _ in range(n+1)]
    before = [0 for _ in range(n+1)]

    for i in range(1, n+1):

        if len(input_list) == 1:
            break
        else:
            if input_list[i-1] < input_list[i]:
                temp = ans[i-1] + 1
                if ans[i] < temp:
                    ans[i] = temp




    


print(dp_14002())




