h,w=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(h)]
global v
v=set()
global on,off
on,off=0,0
def dfs(x,y):
    stack=[(x,y)]
    v.add((x,y))
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    o=l[y][x]
    while stack:
        px,py=stack.pop()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<w and 0<=ny<h and (nx,ny) not in v and l[ny][nx]==o):
                stack.append((nx,ny))
                v.add((nx,ny))
for x in range(w):
    for y in range(h):
        if((x,y) not in v):
            dfs(x,y)
            if(l[y][x]==1):
                off+=1
            else:
                on+=1
print(on,off)
#꺼져있는 것들은 키고 켜져있는 것들은 끄고 그 횟수를 기록하여 풀면 된다.
#전광판 전구 조작
