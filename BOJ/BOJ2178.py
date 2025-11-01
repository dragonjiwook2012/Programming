from collections import deque
m,n=map(int,input().split())
maze=[list(input()) for _ in range(m)]
pos=deque([(0,0,1)])
dx,dy=[1,0,-1,0],[0,1,0,-1]
visited=[[False]*n for _ in range(m)]
visited[0][0]=False
while pos:
    x,y,lv=pos.popleft()
    if(x==n-1 and y==m-1):
        print(lv)
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if(0<=nx<n and 0<=ny<m and maze[ny][nx]=='1' and not visited[ny][nx]):
            visited[ny][nx]=True
            pos.append((nx,ny,lv+1))
#처음으로 풀어본 BFS문제이다(실제로 완전히 처음은 아닌데, 이런 용도로 사용해본적은 처음이다)
#미로 탐색
#실버 1
