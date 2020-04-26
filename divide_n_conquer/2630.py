w_cnt, b_cnt = 0, 0

n = int(input())
M = []

for _ in range(n):
    M.append(list(map(int, input().split())))

def divide_conquer(x, y, N):

    global w_cnt, b_cnt

    tmp_cnt = 0

    for i in range(x, x+N):
        for j in range(y, y+n):
            if M[i][j]:
                tmp_cnt += 1
    
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == N**2:
        b_cnt += 1
    else:
        divide_conquer(x, y, N//2)
        divide_conquer(x + N//2, y, N//2)
        divide_conquer(x, y + N//2, N//2)
        divide_conquer(x + N//2, y + N//2, N//2)
    return

divide_conquer(0,0,n)
print(w_cnt)
print(b_cnt)