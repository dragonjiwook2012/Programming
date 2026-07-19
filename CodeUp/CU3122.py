from collections import deque
n=int(input())
l=[[" "]*(2*n-1) for _ in range(2*n-1)]
def bfs(x,y):
    visited=set([(x,y)])
    q=deque([(x,y,1)])#<- 이걸 스택으로 한 게 문제였다.
    l[y][x]="*"
    dx,dy=[0,1,0,-1],[-1,0,1,0]
    while q:
        px,py,step=q.popleft()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<2*n-1 and 0<=ny<2*n-1 and (nx,ny) not in visited and step<n):
                q.append((nx,ny,step+1))
                l[ny][nx]="*"
                visited.add((nx,ny))
bfs(n-1,n-1)
for i in l:
    print("".join(i))
#좀 고생했다.
#BFS로 해야하는데 DFS로 해버려서 몇 번 틀렸었다..
#마름모 출력하기 2
