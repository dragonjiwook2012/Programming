n=int(input())
d={i:[] for i in range(1,n+1)}
for _ in range(int(input())):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
visited=set()
q=[1]
while q:
    a=q.pop()
    visited.add(a)
    for i in d[a]:
        if(i not in visited):
            q.append(i)
print(len(list(visited))-1)
#그냥 평범한 DFS/BFS 문제이다.
#참고로 이 방식은 BFS이다.
#바이러스
#Silver.2
