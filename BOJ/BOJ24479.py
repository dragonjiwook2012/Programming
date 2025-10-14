import sys
input=sys.stdin.readline
n,m,r=map(int,input().rstrip().split())
graph={i:[] for i in range(1,n+1)}
for _ in range(m):
    u,v=map(int,input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for key in graph:
    graph[key].sort()
l,ans=[r],{i:0 for i in range(1,n+1)}
visited=set()
K=0
while l:#그저 그냥 평범한 DFS..
    k=l.pop()
    if k not in visited:
        K+=1
        ans[k]=K
        visited.add(k)
        for i in reversed(graph[k]):#이부분에서 reversed를 생각해내는게 힘들었다...
            if not i in visited:l.append(i)
for i in range(1,n+1):
    print(ans[i])
#백준 24479 알고리즘 수업 - 깊이 우선 탐색1
#실버 2
