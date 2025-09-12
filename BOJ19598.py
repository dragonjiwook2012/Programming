import sys,heapq
input=sys.stdin.readline
n=int(input().rstrip())
meeting=[0]
l=sorted([tuple(map(int,input().split())) for _ in range(n)])#회의의 시작과 끝을 튜플로 리스트로 만든 후 정렬
for i in range(n):
    f=heapq.heappop(meeting)#가장 빨리 끝나는것을 고름
    if(f>l[i][0]):#만일 그 회의실에서 안되면
        heapq.heappush(meeting,f)#다시 넣음
    heapq.heappush(meeting,l[i][1])#그리고 이번 회의의 끝을 넣음
print(len(meeting))
#최소 회의실 개수
#골드 5
