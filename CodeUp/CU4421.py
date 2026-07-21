n=int(input())
l=[list(map(int,list(input()))) for _ in range(n)]
v=set()
answer=[]
def dfs(x,y):
    ans=1
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    stack=[(x,y)]
    v.add((x,y))
    while stack:
        px,py=stack.pop()
        for i in range(4):
            nx,ny=px+dx[i],py+dy[i]
            if(0<=nx<n and 0<=ny<n and (nx,ny) not in v and l[ny][nx]==1):
                v.add((nx,ny))
                stack.append((nx,ny))
                ans+=1
    return ans
for x in range(n):
    for y in range(n):
        if((x,y) not in v and l[y][x]==1):
            answer.append(dfs(x,y))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
#...그냥 평범하다
#단지 번호 붙이기
