import math,heapq
n,h,t=map(int,input().split())
g=[-int(input()) for _ in range(n)]
heapq.heapify(g)
flag=False
for i in range(t):
    tallest=-1*heapq.heappop(g)#가장 키 큰 거인
    if(tallest<h):#가장 키 큰 거인이 나보다 작으면
        flag=True
        print('YES')#성공
        print(i)#몇번만에 성공했는지
        break
    if(tallest==1):#그게 아닐때 만일 가장 키 큰 거인의 키가 1이면
        heapq.heappush(g,-1)#1 그대로 투입
    else:
        heapq.heappush(g,-1*math.floor(tallest/2))#아닐땐 반으로 쪼개기
if(not flag):#만일 아직 출력을 안했다면
    if(-1*g[0]<h):#성공했다면
        print('YES')#출력
        print(t)
    else:#아닐땐
        print('NO')
        print(g[0]*-1)#가장 큰 거인의 키 출력
#꽤 고생했다. 뿅망치로 찍으면 반으로 나뉘는데 math.floor을 쓰고 1일때만 반례처리로 1로 바꾸는건데 math.ceil을 써버렸다.
#센티와 마법의 뿅망치
#실버 1
#https://www.acmicpc.net/problem/19638
