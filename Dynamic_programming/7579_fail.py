def get_input():

    N, M = map(int, input().split())
   
    mem = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    return N, M, mem, cost

def dp_7579():

    N, M, mem, cost = get_input()

    total = M
    ans= [[0,0]*N]*N #solve this later
    print(ans)
    print(ans[1])

    for i in range(N+1):
         for j in range(N+1):

             ans[i].append(j)


    return ans


            
            




temp = dp_7579()

print(temp)