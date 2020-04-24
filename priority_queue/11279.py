import sys

pq = []
pqlen = 0

n = int(input())

while n > 0:

    n -= 1
    x = int(input())

    if x > 0:

        pq.append(x)
        pqlen += 1
        a = pqlen - 1

        while a > 0:
            if pq[a] > pq[(a-1)//2]:
                pq[a], pq[(a-1)//2] = pq[(a-1)//2] , pq[a]
                a = (a-1)//2
            else: break

    elif x==0:
        
        if pqlen==0:
            print(0)
        else:
            print(pq[0])
            pq=[]
        

    