def get_input():

    n = int(input())

    return n

def dp_12852(n):

    ans = [0 for _ in range(n+1)]
    before = [0 for _ in range(n+1)]

    for i in range(1,n+1):

        if i == 1:
            ans[i] = 0
        else:
            ans[i] = ans[i-1]+1
            before[i] = i-1

            if(i%2 == 0):
                m = int(i/2)
                temp = ans[m] + 1
                if ans[i] > temp:
                    ans[i] = temp
                    before[i] = m
            
            if(i%3 == 0):
                m = int(i/3)
                temp = ans[m] + 1
                if ans[i] > temp:
                    ans[i] = temp
                    before[i] = m

    return ans[n], before

def main():

    n = get_input()
    ans, before = dp_12852(n)
    step = []

    print(ans)
    
    i = n
    step.append(i)

    while i!=1:
        step.append(before[i])
        i = before[i]

    print(*step)

if __name__ == "__main__":
    main()