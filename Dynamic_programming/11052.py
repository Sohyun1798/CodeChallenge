import sys
input = sys.stdin.readline

n = int(input())
inputList = list(map(int, input().rstrip().split()))

value = [0] * (n+1)

for i in range(1, n+1):
    value[i] = inputList[i-1]

dpValue = []



    
