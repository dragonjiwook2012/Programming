l=[list(input()) for _ in range(10)]
x,y=map(int,input().split())
def dfs(x,y):
    l[y][x]="*"
    s=[(x,y)]
    v=set(s)
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    while s:
        px,py=s.pop()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<10 and 0<=ny<10 and (nx,ny) not in v and l[ny][nx]!="*"):
                v.add((nx,ny))
                s.append((nx,ny))
                l[ny][nx]="*"
if(l[y][x]!='*'):
    dfs(x,y)
for i in l:
    print("".join(i))
#이해가 살짝 안돼서 한번 틀렸던 문제
#난이도 자체는 어렵지 않다.
#그림판 채우기
