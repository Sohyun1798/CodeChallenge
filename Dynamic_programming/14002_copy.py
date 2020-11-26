import sys

n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

dp = []
index = [0]*n

for i in range(n):

    if i == 0:
        dp.append(seq[i])

    
    low = 0
    high = len(dp)-1

    while low <= high:
        mid = (low+high)//2
        print("mid=%d", mid)

        if dp[mid] < A[i]:
            low = mid+1
        else:
            high = mid-1
    
    if low >= len(dp):
        index[i] = 
        dp.append()

    low = 0
    high = 
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

l_cnt = max(dp)
print(l_cnt)

idx = dp.index(l_cnt)
aSeq = []

while idx >= 0:
    if dp[idx] == l_cnt:
        aSeq.append(seq[idx])
        l_cnt -= 1
    idx -= 1

print(*aSeq[::-1])