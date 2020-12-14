temp = [1,1,2,2]

max_v = max(temp)
max_i = temp.index(max_v)
print(max_i)

for i in range(N+1):
 
        for j in range(N+1):

            if i == 0:
                if j == 0:
                    ans[i].append([0,0])
                else: ans[i].append([mem[j-1], cost[j-1]])
          
            else:
                if i == j:
                    ans[i].append(ans[i-1][j])
                else:
                    ans[i].append([ans[i-1][j][0]+mem[i-1], ans[i-1][j][1]+cost[i-1]])

        print(ans[i])