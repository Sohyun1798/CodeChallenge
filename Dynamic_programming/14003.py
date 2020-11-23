import sys
 
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
DP=[[-1000000001,-1]]#현재 인덱스 저장
Trace=[0]*N#이전 인덱스가 어디인지 저장
 
 
#2분법을 통해 순서찾기
for i in range(N):
 
    low=0
    high=len(DP)-1
 
    while low<=high:#A[i]보다 작거나 같은수중에 제일 큰거 위치 찾기
        mid=(low+high)//2
        if DP[mid][0]<A[i]:
            low=mid+1
        else:
            high=mid-1
 
    if low>=len(DP):#위치가 배열보다 크다면 넣어준다
        Trace[i]=DP[low-1][1]
        DP.append([A[i],i])
    else:#해당 위치의 숫자를 바꿔준다.항상 작거나 같은수를 반환하기때문에 비교하지 않아도된다.
        DP[low][0]=A[i]
        #현재 인덱스 위치와 이전 인덱스 위치도 같이 저장해준다.
        DP[low][1]=i#현재 인덱스저장
        Trace[i]=DP[low-1][1]#이전 인덱스위치
# print(DP)
# print(Trace)
print(len(DP)-1)# 가장 긴수열 길이
 
result=[]
cur_index=DP[len(DP)-1][1]#처음 인자 넣기
# result.append(DP[len(DP)-1][0])
while cur_index!=-1:#추적하여 넣기
    result.append(A[cur_index])
    cur_index=Trace[cur_index]
 
for i in range(len(result)-1,-1,-1):#반대로 출력
    print(result[i],end=" ")