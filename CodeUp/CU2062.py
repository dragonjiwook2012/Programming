h,w=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(h)]
v=set()
def dfs(x,y,H):
	s=[(x,y)]
	dx,dy=[1,0,-1,0],[0,1,0,-1]
	v.add((x,y))
	ans=1
	while s:
		px,py=s.pop()
		for i in range(4):
			nx,ny=px+dx[i],py+dy[i]
			if(0<=nx<w and 0<=ny<h and l[ny][nx]==H and (nx,ny) not in v):
				ans+=1
				s.append((nx,ny))
				v.add((nx,ny))
	return ans
hs=set()
for i in l:
	for j in i:
		hs.add(j)
for i in hs:
	if(i!=-1):
		ans=0
		for x in range(w):
			for y in range(h):
				if(l[y][x]==i and (x,y) not in v):
					ans=max(ans,dfs(x,y,i))
		print(i,ans)
#평범.
#Up 2
