l=[list(map(int,input().split())) for _ in range(7)]
v=set()
ans=0
def dfs(x,y,col):
	v.add((x,y))
	s=[(x,y)]
	dx,dy=[0,1,0,-1],[1,0,-1,0]
	t=1
	while s:
		px,py=s.pop()
		for i in range(4):
			nx,ny=px+dx[i],py+dy[i]
			if(0<=nx<=6 and 0<=ny<=6 and l[ny][nx]==col and (nx,ny) not in v):
				s.append((nx,ny))
				v.add((nx,ny))
				t+=1
	if(t>=3):
		return True
	return False
for x in range(7):
	for y in range(7):
		if((x,y) not in v):
			if(dfs(x,y,l[y][x])):
				ans+=1
print(ans)
#다 순회하면서 3개 이상 모여있는것만 확인하면 된다.
#캔디팡
