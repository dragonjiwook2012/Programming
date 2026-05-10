import sys
from bisect import bisect_right,insort
input=sys.stdin.readline#많은 입력을 빨리 처리하기 위해 함수 변형
n=int(input().rstrip())
l=[]
d={i:0 for i in range(n)}#카운터
for _ in range(n):
    a,_=map(int,input().rstrip().split())#y레벨,x레벨은 모두 오름차순이니 y레벨은 무쓸모
    cnt=bisect_right(l,a)#전의 x레벨중 현재 x레벨보다 작거나 같으면 된다
    d[cnt]+=1#카운터 처리
    insort(l,a)#어떻게 보면 추가+정렬이지만 이진탐색을 통해 훨씬 적은 시간 복잡도를 사용했다.
for i in range(n):
    print(d[i])
#이진 탐색만 생각하면 어렵지 않게 풀 수 있을 듯 하다
#Platinum.5
#점의 레벨(별)
