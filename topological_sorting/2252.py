def getInput():

    N, M = map(int, input().split())
    sList = []

    for _ in range(M):
        sList.append(list(map(int, input().split())))

    return N, M, sList

def TS_2252():

    N, M, sList = getInput()

    topolSort = [i for i in range(1, N+1)]

    return topolSort







