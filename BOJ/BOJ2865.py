n,k=map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(n)]#튜플로 저장
dp=[0]*(k+1)#각 무게당 최대 행복
for w,v in l:#모든 물건에 대해 탐색
    for j in range(k,w-1,-1):#최대 무게부터 지금 무게까지 역순으로 탐색
        dp[j]=max(dp[j],dp[j-w]+v)#dp[j]는 현상태(dp[j])와 dp[j-w]+v 중 더 좋은걸 선택
print(dp[k])#k에서 최대 행복 출력
