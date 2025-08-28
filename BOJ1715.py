import sys
import heapq
input=sys.stdin.readline
n=int(input().rstrip())
cards=[]
ans=0
for _ in range(n):
    heapq.heappush(cards,int(input().rstrip()))
while len(cards)>=2:
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)
    ans+=a+b
    heapq.heappush(cards,a+b)
print(ans)
#백준 1715
#카드정렬하기
