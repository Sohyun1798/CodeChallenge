import sys

input = sys.stdin.readline

n = int(input())
sList = []

for _ in range(n):
    sList.append(int(input()))

ans = 0

for i in range(1, n):
    if sList[i-1] > sList[i]:
        ans += 1

print(ans)
    
