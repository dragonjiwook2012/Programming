from collections import deque
w,h=map(int,input().split())
l=list(list(input().split()) for _ in range(h))
visited=set()
def bfs(pos):
    x,y=pos[0],pos[1]
    dx,dy=[1,0,-1,0,1,1,-1,-1],[0,1,0,-1,1,-1,1,-1]
    q=deque([(x,y)])
    while q:
        px,py=q.popleft()
        for i in range(8):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<w and 0<=ny<h and l[ny][nx]=="L"):
                if((nx,ny) not in visited):
                    visited.add((nx,ny))
                    q.append((nx,ny))
ans=0
for x in range(w):
    for y in range(h):
        if(l[y][x]=="L" and (x,y) not in visited):
            visited.add((x,y))
            bfs((x,y))
            ans+=1
print(ans)
#그냥 평범한 BFS/DFS 문제..
#호수의 수 구하기
