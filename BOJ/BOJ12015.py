import bisect#이분탐색
x=int(input())
arr=list(map(int, input().split()))
dp=[arr[0]]
for i in range(x):
    if arr[i]>dp[-1]:#마지막으로 dp에 들어간 수(dp에서 가장 큰 수)가 자신보다 작다면
        dp.append(arr[i])#dp에 자신도 추가
    else:#작거나 같다면
        idx=bisect.bisect_left(dp, arr[i])#dp에 넣을 위치를 bisect으로 찾고
        dp[idx]=arr[i]#그 위치값을 자신으로 변경
print(len(dp))#길이 출력
#백준 12015
#가장 긴 증가하는 부분 수열2
#LIS 1,2,3 모두  이 코드로 풀 수 있음
