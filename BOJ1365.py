import bisect
x=int(input())
arr=list(map(int, input().split()))
dp=[arr[0]]
for i in range(x):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
    else:
        idx=bisect.bisect_left(dp, arr[i])
        dp[idx]=arr[i]
print(len(arr)-len(dp))
#1        4 
#2        1
#3        2
#4        3
#라고 한다면 가장 긴 증가하는 부분수열(1,2,3)은 제거할 필요가 없고, 그 부분수열에 포함되지 않는 4만 제거하면 된다.
#백준 1365
#꼬인 전깃
