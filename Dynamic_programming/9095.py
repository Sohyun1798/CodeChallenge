test_case=int(input())

input_list=[]
for i in range(test_case):
    input_list.append(int(input()))

dp=[1,2,4]

for i in range(3,max(input_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp)

for i in input_list:
    print(dp[i-1])