from collections import deque
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
def bfs():
    q=deque([(0,0,1)])
    v=set([(0,0)])
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    while q:
        px,py,t=q.popleft()
        if(px==m-1 and py==n-1):
            return t
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<m and 0<=ny<n and abs(l[py][px]-l[ny][nx])<=1 and (nx,ny) not in v):
                q.append((nx,ny,t+1))
                v.add((nx,ny))
    return 0
print(bfs())
#제목이랑 문제 내용이랑 상관이 없는 것...같다.
#놀이공원
