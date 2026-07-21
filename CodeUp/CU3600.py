from collections import deque
n=int(input())
kr,kc=map(int,input().split())
tr,tc=map(int,input().split())
def bfs():
    q=deque([(kr,kc,0)])
    v=set([(kr,kc)])
    dx,dy=[1,2,2,1,-1,-2,-2,-1],[2,1,-1,-2,-2,-1,1,2]
    while q:
        px,py,t=q.popleft()
        if(px==tr and py==tc):
            return t
        for i in range(8):
            nx,ny=px+dx[i],py+dy[i]
            if(1<=nx<=n and 1<=ny<=n and (nx,ny) not in v):
                q.append((nx,ny,t+1))
                v.add((nx,ny))
print(bfs())
#평범한 BFS(말은 나이트를 의미함)
#체스 말 이동
