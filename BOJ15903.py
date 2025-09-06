import heapq#1715번과 비슷한 알고리즘이다
n,m=map(int,input().split())
l=list(map(int,input().split()))
heapq.heapify(l)
for _ in range(m):
    f,s=heapq.heappop(l),heapq.heappop(l)#가장 작은 두 값을 가져오고
    heapq.heappush(l,f+s)#그 합을 다시 넣는다
    heapq.heappush(l,f+s)#두번
print(sum(l))
#백준 15903
#카드합체놀이
#실버 1
