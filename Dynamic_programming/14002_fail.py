def get_input():

    n = int(input())

    input_list = []
    input_list.extend(list(map(int, input().split())))
    
    return n, input_list

def dp_14002(n, input_list):

    ans = [1 for _ in range(n+1)]
    before = [0 for _ in range(n+1)]

    for i in range(n):
        for j in range(i):

            if input_list[i] > input_list[j]:
                if ans[j+1]+1 > ans[i+1]:
                    ans[i+1] = ans[j+1]+1
                    before[i+1] = j+1

    print(before)
    return ans[n], before

def main():

    n, input_list = get_input()
    ans, before = dp_14002(n, input_list)
    step = []

    print(ans)

    i = n

    while i!=1:
        step.append(input_list[before[i]])
        i = before[i]

    print(*step)

if __name__ == "__main__":
    main()
