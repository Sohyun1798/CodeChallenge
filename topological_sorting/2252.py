def getInput():

    N, M = map(int, input().split())
    sList = []

    for _ in range(M):
        sList.append(list(map(int, input().split())))

    return N, M, sList

def TS_2252():

    N, M, sList = getInput()

    topolSort = [i for i in range(1, N+1)]

    for i in range(M):

        A = sList[i][0]
        B = sList[i][1]
        Aidx = topolSort.index(A)
        Bidx = topolSort.index(B)

        if Aidx > Bidx:
            topolSort[Bidx] = A
            topolSort[Aidx] = B

    return topolSort

print(TS_2252())







