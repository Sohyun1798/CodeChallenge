def get_input():

    N, M = map(int, input().split())
   
    mem = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    return N, M, mem, cost

def dp_7579():

    N, M, mem, cost = get_input()

    total = M
    ans= [[]*N]*N
    print(ans)
    print(ans[1])

    for i in range(N):
        for j in range(N):

            if i == 0:
                if j == 0:
                    ans[i].append([0,0])
                else: ans[i].append([mem[i]+mem[j], cost[i]+cost[j]])
          
            else:
                if i == j:
                    ans[i].append(ans[i-1][j])
                else:
                    ans[i].append([ans[i-1][j][0]+mem[j], ans[i-1][j][1]+cost[j]])

    return ans


            
            




temp = dp_7579()

print(temp[1])