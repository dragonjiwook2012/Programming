from collections import deque
n=int(input())
x,y=map(int,input().split())
l=[[0]*n for _ in range(n)]
l[x-1][y-1]=1
def bfs(x,y):
	q=deque([(x,y,1)])
	visited=set([(x,y)])
	dx,dy=[1,0,-1,0],[0,1,0,-1]
	while q:
		px,py,h=q.popleft()
		for i in range(4):
			nx,ny=px+dx[i],py+dy[i]
			if(0<=nx<n and 0<=ny<n and(nx,ny) not in visited): 
				l[nx][ny]=h+1
				q.append((nx,ny,h+1))
				visited.add((nx,ny))
bfs(x-1,y-1)
for i in l:
	print(*i)
#전에 풀었던 마름모 출력하기랑 비슷한 느낌..?
#숫자 등고선
