from collections import deque
m,n,h=map(int,input().split())
l=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
rt=[]
for x in range(m):
    for y in range(n):
        for z in range(h):
            if(l[z][y][x]==1):
                rt.append((x,y,z))
def bfs():
    q=deque([(x,y,z,0) for x,y,z in rt])
    v=set(rt)
    dx,dy,dz=[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
    ld=0
    while q:
        px,py,pz,d=q.popleft()
        ld=d
        for i in range(6):
            nx,ny,nz=px+dx[i],py+dy[i],pz+dz[i]
            if(0<=nx<m and 0<=ny<n and 0<=nz<h and (nx,ny,nz) not in v and l[nz][ny][nx]==0):
                l[nz][ny][nx]=1
                q.append((nx,ny,nz,d+1))
                v.add((nx,ny,nz))
    for x in range(m):
        for y in range(n):
            for z in range(h):
                if(l[z][y][x]==0):
                    return -1
    return ld
print(bfs())
#3차원 축만 잘 알고 만들면 나름대로 할만 하다.
#토마토(초등)
