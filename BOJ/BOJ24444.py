import sys
from collections import deque
input=sys.stdin.readline
n,m,r=map(int,input().rstrip().split())
graph={i:[] for i in range(1,n+1)}
for _ in range(m):
    u,v=map(int,input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for key in graph:
    graph[key].sort()
l,ans=deque([r]),{i:0 for i in range(1,n+1)}
visited=set()
K=0
while l:
    k=l.popleft()
    if k not in visited:
        K+=1
        ans[k]=K
        visited.add(k)
        for i in graph[k]:
            if not i in visited:l.append(i)
for i in range(1,n+1):
    print(ans[i])
#꽤 쉽게 풀었다 24479번을 먼저 풀어서 stack만 queue로 교체해주고 reversed만 빼면 이 문제가 풀린다.
#백준 24444 알고리즘 수업 - 너비 우선 탐색
#실버 2
