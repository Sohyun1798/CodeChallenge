def get_input():

    n = int(input())
    input_tri = []

    for _ in range(n):
        input_tri.append(list(map(int, input().split())))
    
    return n, input_tri

def dynamic_program():
    
    n, input_tri = get_input()
    ans = []

    for i in range(1,n+1):
        ans.append([0 for _ in range(i)])


    for i in range(n):
        if i == 0:
            ans[0][0] = input_tri[0][0]
        else:
            for k in range(i+1):
                if k == 0:
                    ans[i][k] = ans[i-1][k]+input_tri[i][k]
                elif k == i:
                    ans[i][k] = ans[i-1][k-1]+input_tri[i][k]
                else:
                    if ans[i-1][k-1] > ans[i-1][k]:
                        ans[i][k] = ans[i-1][k-1] + input_tri[i][k]
                    else: ans[i][k] = ans[i-1][k] + input_tri[i][k]

    return max(ans[n-1])

def main():
    print(dynamic_program())

if __name__ == "__main__":
    main()



