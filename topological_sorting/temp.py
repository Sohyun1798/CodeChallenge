def getInput():

    N, M = map(int, input().split())
    sList = []

    for _ in range(M):
        sList.append(list(map(int, input().split())))

    return N, M, sList

N, M, sList = getInput()
topolSort = {}
queue = []
ans = []

for i in range(1, N+1):
    topolSort[i] = 0

for j in range(M):
    topolSort[sList[j][1]] += 1

def TS_2252():

    global queue
    global ans

    for i in range(1, N+1):
        if topolSort[i] == 0 and i not in ans and i not in queue:
            queue.append(i)

    while queue:
        
        temp = queue.pop(0)

        for j in range(M):
            if sList[j][0] == temp:
                topolSort[sList[j][1]] -= 1

        ans.append(temp)
        TS_2252()
      
    return ans

print(*TS_2252())

