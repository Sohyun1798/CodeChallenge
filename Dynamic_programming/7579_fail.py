def get_input():

    N, M = map(int, input().split())
   
    mem = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    return N, M, mem, cost

def dp_7579():

    N, M, mem, cost = get_input()

    total = M
    table = []
    print(table)

    for i in range(N+1):
        temp = []

        for j in range(N+1):

            if i == 0:
                if j == 0:
                    temp.append(0)
                else: temp.append(mem[j-1])
            
            else:
                if i == j:
                    temp.append(table[i-1][j])
                else:
                    temp.append(table[i-1][j] + mem[i-1])

        if min(temp) >= M:
            break

        else: table.append(temp)
                   
    return table



temp = dp_7579()

print(temp)