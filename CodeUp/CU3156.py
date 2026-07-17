from collections import deque
w,h=map(int,input().split())
l=[list(map(int,list(input()))) for _ in range(h)]
ans=0
v=set()
def bfs(v,x,y,w,h,l):
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    q=deque([(x,y)])
    v.add((x,y))
    ans=1
    is_river=False
    while q:
        px,py=q.popleft()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<=w-1 and 0<=ny<=h-1):
                if(l[ny][nx]==2):
                    is_river=True
                if((nx,ny) not in v and l[ny][nx]==0):
                    q.append((nx,ny))
                    v.add((nx,ny))
                    ans+=1
    if(is_river):return 0,v
    return ans,v
ap=(-1,-1)
for x in range(w):
    for y in range(h):
        if(l[y][x]==0 and (x,y) not in v):
            a,v=bfs(v,x,y,w,h,l)
            ans=max(a,ans)
print(ans)
#강...이라는 조건때문에 틀릴 뻔 했다.(사실 한 번 틀림)
#그래도 그것만 이해하고 BFS 할 줄 알면 나쁘지 않았다.
#도시 계획 2
