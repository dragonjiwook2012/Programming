def dfs(pos,l,n,m):
    cnt=1
    v.add(pos)
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    s=[pos]
    while s:
        a=s.pop()
        for i in range(4):
            nx,ny=a[0]+dx[i],a[1]+dy[i]
            if((nx,ny) not in v and 0<=nx<=n-1 and 0<=ny<=m-1 and l[ny][nx]==0):
                v.add((nx,ny))
                cnt+=1
                s.append((nx,ny))
    return cnt
m,n,k=map(int,input().split())
l=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    a,b,c,d=map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            l[y][x]=1
global v
cnt=0
ans=[]
v=set()
for y in range(m):
    for x in range(n):
        if((x,y) not in v and l[y][x]==0):
            ans.append(dfs((x,y),l,n,m))
            cnt+=1
print(cnt)
print(*sorted(ans))
