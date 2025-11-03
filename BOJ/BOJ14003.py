from bisect import bisect_left
x=int(input())
l=[0]+list(map(int,input().split()))
dp=[0 for _ in range(x+1)]
maxVal=0
tmp=[-1000000001]#임시로 추가한 수(-1000000001)
for i in range(1,x+1):#-1000000001빼고 각각 진행
    if(tmp[-1]<l[i]):#만일 부분 수열에서 이 수가 가장 크다면
        tmp.append(l[i])#추가하고
        dp[i]=len(tmp)-1#아까 그 -1000000001의 길이는 빼고 dp에 입력
        maxVal=max(maxVal,dp[i])#가장 긴 길이도 수정
    else:
        dp[i]=bisect_left(tmp,l[i])#아니라면 이 수가 들어갈 위치 확인
        tmp[dp[i]]=l[i]#그 위치의 값을 변경
tmp2=[]#LIS
print(maxVal)#일단 먼저 출력
for i in range(x,0,-1):#거꾸로 순회하기!
    if(dp[i]==maxVal):#만일 가장 길때의 그 값이라면
        tmp2.append(l[i])#LIS에 추가하고
        maxVal-=1#목표값 1 줄이기
print(*tmp2[::-1])#뒤집어서 출력!
#진짜 다사다난했던 문제다. 바로 전 문제에 썼던 코드(with dp)를 복붙해봤지만 실패했고 겨우겨우 푸는 방법을 찾아서 겨우 이해했다
#약간 전체적으로 dp느낌인데 bisect을 활용해서 O(N^2)가 아니도록(2중 for문을 없앰) 만든 느낌이였다.
#처음으로 풀이에 성공한 플래니텀 문제다!
#플래티넘 5
#가장 긴 증가하는 부분수열 5
