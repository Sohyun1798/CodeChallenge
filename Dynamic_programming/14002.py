def get_input():

    n = int(input())

    input_list = []
    input_list.extend(list(map(int, input().split())))
    
    return n, input_list

def dp_14002():

    n, input_list = get_input()

    ans = [0 for _ in range(n+1)]
    before = [0 for _ in range(n+1)]

    for i in range(n):
        for j in range(i):

            if input_list[i] > input_list[j]:
                




    


print(dp_14002())




