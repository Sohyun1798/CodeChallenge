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
        for j in range(1, i):




    


print(dp_14002())




