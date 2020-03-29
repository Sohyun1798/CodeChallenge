import numpy as np

N = int(input())
check = np.zeros(N,N)

def n_queen(s, n, check):

    for i in range(s,n):
        for j in range(s,n):
            if check[i][j] == 1:
                continue
            check[i][0:n] = 1
            check[0:n][j] = 1
        
        n_queen(s+1, n, check)



    pass


check = []