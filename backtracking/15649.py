def get_input():

    N, M = map(int, input().split())

    return N, M

def back_tracking(index, N, M, answer, check):

    if index == M:
        for i in range(M):
            print(answer[i], end = ' ')
        print()

        return

    for i in range(1, N+1):
        if check[i]:
            continue
        check[i] = True
        answer[index] = i
        back_tracking(index+1, N, M, answer, check)
        check[i] = False

def main():

    n, m = get_input()

    check = [False]*(n+1)
    answer = [0]*m

    back_tracking(0,n,m,answer,check)

if __name__ == "__main__":
    main()
