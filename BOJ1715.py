import sys
import heapq
input=sys.stdin.readline
n=int(input().rstrip())
cards=[]
ans=0
for _ in range(n):
    heapq.heappush(cards,int(input().rstrip()))
while len(cards)>=2:
    a=heapq.heappop(cards)#가장 작은 카드 장수 고르고
    b=heapq.heappop(cards)#또 가장 작은 카드 장수를 고름
    ans+=a+b#더해서
    heapq.heappush(cards,a+b)#넣으면 됨
print(ans)
#백준 1715
#카드정렬하기
