import sys

input = sys.stdin.readline

n = int(input())
table = []

sectorFP = [[0,0,0]] * n

for _ in range(n):
    table.append(list(input().rstrip().split()))

for i in range(n):
    if i == 0:
        if 'R' in table[0]:
            sectorFP[0][0] = 1
        if 'G' in table[0]:
            sectorFP[0][1] = 1
        if 'B' in table[0]:
            sectorFP[0][2] = 1

    else:
        if 'R' in table[i]:
            if sectorFP[i-1][0] != 0:
                sectorFP[i][0] = sectorFP[i-1][0]
            else: sectorFP[i][0] = 1
        


