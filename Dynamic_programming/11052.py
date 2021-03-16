import sys
input = sys.stdin.readline

n = int(input())
inputList = [0] + list(map(int, input().rstrip().split()))

value = [0] * (n+1)

value[1] = inputList[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if value[i] < value[i-j] + inputList[j]:
            value[i] = value[i-j] + inputList[j]

print(value[n])
        



    
