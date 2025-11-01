from collections import deque
n,m=map(int,input().split())
pos=deque([(n,0)])
visited=[False]*100001
visited[n]==True
while pos:
    p=pos.popleft()
    if(p[0]==m):
        print(p[1])
        break
    if(p[0]+1<=100000 and not visited[p[0]+1]):
        pos.append((p[0]+1,p[1]+1))
        visited[p[0]+1]=True
    if(p[0]-1>=0 and not visited[p[0]-1]):
        pos.append((p[0]-1,p[1]+1))
        visited[p[0]-1]=True
    if(p[0]*2<=100000 and not visited[p[0]*2]):
        pos.append((p[0]*2,p[1]+1))
        visited[p[0]*2]=True
#간단한 BFS 문제다.
#숨바꼭질
#실버 1
