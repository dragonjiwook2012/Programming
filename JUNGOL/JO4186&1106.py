import sys
from collections import deque
n,m=map(int,input().split())
a,b,py,px=map(int,input().split())
q=deque([(b-1,a-1,0)])
v=[[False for _ in range(m)] for _ in range(n)]
v[a-1][b-1]=True
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]
found=False
while q:
    pos=q.popleft()
    if(pos[0]==px-1 and pos[1]==py-1):
        print(pos[2])
        found=True
        break
    for i in range(8):
        nx,ny=pos[0]+dx[i],pos[1]+dy[i]
        if(0<=nx<m and 0<=ny<n and not v[ny][nx]):
            q.append((nx,ny,pos[2]+1))
            v[ny][nx]=True
            if(nx==px-1 and ny==py-1):
                print(pos[2]+1)
                found=True
                break
    if(found):break
#실버 1인데도... 꽤 힏들었다.(사실 문제를 잘못 읽었음...)
#참고로 제목이 4186이랑 1106인 이유는 둘 다 이 코드로 깨지기 때문이다
#장기/장기 2
#Silver.1
