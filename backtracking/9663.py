n = int(input())
ans = 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def n_queen(i):

    global ans

    if i == n:
        ans += 1
        return

    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            n_queen(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

n_queen(0)
print(ans)





