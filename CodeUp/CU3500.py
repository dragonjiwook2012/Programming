l=[list(map(int,input().split())) for _ in range(9)]
c=[[False]*9 for _ in range(9)]
ansl=[[0]*9 for _ in range(9)]
y,x=map(int,input().split())
def dfs(x,y):
    s=[(x,y)]
    v=set([(x,y)])
    dx,dy=[1,0,-1,0,1,1,-1,-1],[0,1,0,-1,1,-1,1,-1]
    while s:
        px,py=s.pop()
        for i in range(8):
            nx,ny=px+dx[i],py+dy[i]
            append=True
            if(0<=nx<9 and 0<=ny<9):
                for j in range(8):
                    nnx,nny=nx+dx[j],ny+dy[j]
                    if(0<=nnx<9 and 0<=nny<9 and l[nny][nnx]==1):
                        append=False
                        break
            if(0<=nx<9 and 0<=ny<9 and (nx,ny) not in v and l[ny][nx]!=1):
                if(append):
                    s.append((nx,ny))
                    v.add((nx,ny))
                c[ny][nx]=True
if(l[y-1][x-1]==1):
    for i in range(9):
        for j in range(9):
            if(i==x-1 and j==y-1):
                ansl[j][i]="-1"
            else:
                ansl[j][i]="_"
else:
    c[y-1][x-1]=True
    dx,dy=[1,0,-1,0,1,1,-1,-1],[0,1,0,-1,1,-1,1,-1]
    b=False
    for i in range(8):
        nx,ny=x+dx[i]-1,y+dy[i]-1
        if(0<=nx<9 and 0<=ny<9 and l[ny][nx]==1):
            b=True
            break
    if(not b):dfs(x-1,y-1)
    for i in range(9):
        for j in range(9):
            if(l[j][i]==1):
                for idx in range(8):
                    nx,ny=i+dx[idx],j+dy[idx]
                    if(0<=nx<9 and 0<=ny<9 and l[ny][nx]==0 and c[ny][nx]):
                        ansl[ny][nx]+=1
                ansl[j][i]="_"
            if(not c[j][i]):
                ansl[j][i]="_"
for i in ansl:
    print(*i)
#보이는 것처럼 너무 복잡했다...
#실제 지뢰찾기 게임을 해본적 없어서 더 그랬던 것 같다.
#지뢰찾기 2
