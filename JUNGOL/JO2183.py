from itertools import permutations
n=int(input())
l=list(input().split())
pl=permutations(l,n)#모든 경우의 수를 만든다
ans=[]
for p in pl:
    t=""
    for i in p:
        t+=i#그걸 다 연결한 후 
    ans.append(t)#리스트에 넣고
print(max(ans))#가장 큰 값을 프린트한다.
#처음에는 맨 첫 자리수를 이용해 sort하고 풀었는데 2,24같은게 포함되어 있으면 값이 이상하게 나오기도 해서
#그냥 막 해본다 생각하면서 해본건데... 성공했다.
#참고로 max는 꼭 안이 int가 아니여도 상관 없고 가장 큰 값을 반환한다.(길이가 모두 같아서)
#이게... 플래티넘?
#Platinum.5
#가장 큰 값 만들기
#https://jungol.co.kr/problem/2183
