from collections import deque
global m,p,n
n=int(input())
m=[list(map(int,list(input().rstrip()))) for _ in range(n)]
p=[]
for i in range(n):
    for j in range(n):
        if(m[i][j]==1):
            p.append((j,i))
cnt=0
ans=[]
def dfs(pos,i):
    m[pos[1]][pos[0]]=i
    q=deque([pos])
    cnt=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    while q:
        d=q.pop()
        for a in range(4):
            nx,ny=d[0]+dx[a],d[1]+dy[a]
            if(0<=nx<=n-1 and 0<=ny<=n-1 and m[ny][nx]==1):
                m[ny][nx]=i
                q.append((nx,ny))
                cnt+=1
                # print(p,(nx,ny))
                if((nx,ny) in p):p.remove((nx,ny))
    return cnt
while p:
    cnt+=1
    a=p.pop()
    k=dfs(a,2)
    ans.append(k)
print(cnt)
ans.sort()
for i in ans:
    print(i)
#dfs/bfs 문제는 오랫만에 하고 잘 기억이 안나서 뭔가 다른 사람 코드랑 다르게 풀긴 했다.
#단지번호 붙이기
#Silver.1
