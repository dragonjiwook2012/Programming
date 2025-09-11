import heapq,sys#처음에 시간초과로 틀렸었는데...
input=sys.stdin.readline#input() 만 sys.stdin.readline()으로 바꿔줬더니 맞았다....
n=int(input().rstrip())
cl=[tuple(map(int,input().rstrip().split())) for _ in range(n)]
cl.sort()
rooms=[]
for s,e in cl:
    if(rooms and rooms[0]<=s):
         heapq.heappop(rooms)
    heapq.heappush(rooms,e)
print(len(rooms))
#강의실배정
#골드 4
