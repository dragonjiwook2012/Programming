from collections import deque
w,h=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(h)]
def bfs(l,f,w,h):
    q=deque(f)
    v=set()
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    dist=[[-1 for _ in range(w)] for _ in range(h)]
    for x,y in f:
        dist[y][x]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if((nx,ny) not in v and 0<=nx<=w-1 and 0<=ny<=h-1 and l[ny][nx]==0):
                l[ny][nx]=1
                q.append((nx,ny))
                v.add((nx,ny))
                dist[ny][nx]=dist[y][x]+1
        v.add((x,y))
    all_ripen=True
    M_day=0
    for i in range(w):
        for j in range(h):
            if(l[j][i]==0):
                all_ripen=False
            M_day=max(M_day,dist[j][i])
    if(not all_ripen):
        print(-1)
    else:
        print(M_day)
f=[]
for x in range(w):
	for y in range(h):
		if(l[y][x]==1):
			f.append((x,y))
bfs(l,f,w,h)
#프로그래밍 학원을 다니며 처음으로 접해봤는데, 코드업도 나름대로 좋은 것 같다.
#코드업은 번호로 문제의 수준이나 분류가 나뉘는건 좋지만(예: 6000대는 Python 연습용 등) 코드업 오리지널 문제가 별로 안 보이고, 뭔가 어디선가 본 거 같은 문제가 많은 점이 아쉬웠다.(그리고 문제에 백준이나 정올처럼 랭크가 없음)
#이거는 처음에는 그냥 BFS/DFS 없이 해보려고 하다가 어딘가 잘못돼서 결국 BFS로 했다.
#토마토(고등)
