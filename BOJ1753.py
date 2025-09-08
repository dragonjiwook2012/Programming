import heapq,sys
input=sys.stdin.readline
u,v=map(int,input().rstrip().split())
distance=[float('INF')]*u#거리 모두 무한
start=int(input())
graph={i:[] for i in range(1,u+1)}
for _ in range(v):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
q=[]
heapq.heappush(q,(0,start))
distance[start-1]=0
while q:
    dist,now=heapq.heappop(q)
    if(distance[now-1]<dist):#전이 지금보다 낫다면
        continue#넘어가기
    for i in graph[now]:#아니라면 모든 경로들을
        cost=dist+i[1]#원래 경로에 더해서
        if(cost<distance[i[0]-1]):#이게 더 짧다면
            distance[i[0]-1]=cost#수정
            heapq.heappush(q,(cost,i[0]))#그리고 q에 삽입
for i in range(u):
    if(distance[i]==float('INF')):
        print('INF')
    else:
        print(distance[i])
#백준 1753
#최단경로
#골드 4
