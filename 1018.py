import numpy

def get_input():

    N = input()
    M = input()

    matrix = np.zeros(N,M)
    
    for i in range(N):
        for j in range(M):
            matrix[i][j] = input()

    return matrix

def count_WB():

    matrix = get_input()

    cnt = 0

    for i in range(N): #
        for j in range(M): #
            
            if (i+1)%2 == 1:
                temp = matrix[i][j]

                if temp == "W" and (j+1)%2 == 1:

            elif (i+1)%2==1 and temp == "W":

def count_BW():
    










