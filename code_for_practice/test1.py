def solution(A):

    ans = 0
    
    for i in A:
        if i in range(0, 10) and i > ans:
            ans = i

    return ans

A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]

print(solution(A))
