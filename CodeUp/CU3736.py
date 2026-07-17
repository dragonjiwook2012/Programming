import bisect
n=int(input())
l=list(map(int,input().split()))
dp=[l[0]]
for i in l:
	if(dp[-1]<i):
		dp.append(i)
	else:
		ind=bisect.bisect_left(dp,i)
		dp[ind]=i
print(len(dp))
#사실 이건 옛날에 풀었던 거라서 꽤 쉬웠다.
#푸는 방법은 dp랑 dp+bisect 있지만 나는 더 빠른 dp+bisect를 썼다.
#LIS (Large)
