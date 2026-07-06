import heapq
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for _ in range(len(l)-1):
    a,b=heapq.heappop(l),heapq.heappop(l)
    ans+=a+b
    heapq.heappush(l,a+b)
print(ans)
#전형적인 heapq 문제이다.
#물론 정렬만 하거나 min으로 찾는 방법도 있지만, 태그에 우선순위 큐(heapq)가 있길래 그냥 heapq로 풀었다.
#이 밑에는 그냥 정렬로 푸는 방법이다.
#이 코드는 아무래도 좀 느릴 것 같다...
n=int(input())
l=list(map(int,input().split()))
ans=0
for _ in range(n-1):
  l.sort(reverse=True)
  a,b=l.pop(),l.pop()
  ans+=a+b
  l.append(a+b)
print(ans)

#골드 4...라기엔 너무 쉽다.
#모두 더하기
#Gold.4
