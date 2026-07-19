n=int(input())
l=list(list(map(int,input().split())) for _ in range(n))
M=0
for i in l:
    for j in i:
        M=max(M,j)
ans=1
def dfs(x,y,v,h):
    v.add((x,y))
    stack=[(x,y)]
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    while stack:
        px,py=stack.pop()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<n and 0<=ny<n and l[ny][nx]>h and (nx,ny) not in v):
                v.add((nx,ny))
                stack.append((nx,ny))
    return v
for h in range(0,M):
    visited=set()
    a=0
    for x in range(n):
        for y in range(n):
            if(l[y][x]>h and (x,y) not in visited):
                v=dfs(x,y,visited,h)
                a+=1
    ans=max(ans,a)
print(ans)
#그냥 높이마다 하나씩 DFS/BFS로 찾아보면 된다.
#안전 영역
