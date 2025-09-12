import sys,heapq
input=sys.stdin.readline
t=int(input().rstrip())
mod=1000000007
for _ in range(t):
    ans=1
    n=int(input())
    l=list(map(int,input().split()))
    heapq.heapify(l)
    for i in range(n-1):
        f,s=heapq.heappop(l),heapq.heappop(l)
        ans=(ans*f*s)%mod
        heapq.heappush(l,(f*s))
    print(ans%mod)
#전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
#느낌은 카드정렬하기 문제의 곱하기버전? 느낌이였다
#골드4
