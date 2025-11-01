import sys
input=sys.stdin.readline
n=int(input().rstrip())
l=[list(map(int,input().split())) for _ in range(n)]
dp=[[-1]*i for i in range(1,n+1)]#dp 테이블 -1
dp[0][0]=l[0][0]#맨 윗칸은 고정
for i in range(n-1):
    nl=l[i]
    for j in range(len(nl)):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j]+l[i+1][j])#바로 밑 칸
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+l[i+1][j+1])#오른쪽 아래 대각선
print(max(dp[-1]))
#생각보다 유명한 문제인데도 꽤 힘들었다...
#정수 삼각형
#실버 1
