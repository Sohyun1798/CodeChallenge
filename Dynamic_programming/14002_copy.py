import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
DP = [[-1000000001, -1]]
Trace = [0]*N

for i in range(N):

    low = 0
    high = len(DP)-1

    while low <= high:
        mid = (low+high)//2
        if DP[mid][0] < A[i]:
            low = mid+1
        else:
            high = mid-1

    if low >= len(DP):
        Trace[i] = DP[low-1][1]
        DP.append([A[i],i])
    else:
        DP[low][0] = A[i]
        DP[low][1] = i
        Trace[i] = DP[low-1][1]

        