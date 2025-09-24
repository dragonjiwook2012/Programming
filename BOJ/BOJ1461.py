n,m=map(int,input().split())
arr=list(map(int,input().split()))+[0]
arr.sort()
Pos=arr.index(0)
neg=arr[:Pos]#음수와
pos=arr[Pos+1:]#양수 리스트로 나누고
pos=pos[::-1]#양수리스트는 내림차순으로 바꾼다.
ans=0
for i in range(0,len(neg),m):#m개씩 집은다음 갔다가 와야 하니까 *2를 한다.
    ans+=abs(neg[i])*2
for i in range(0,len(pos),m):#얘도 마찬가지
    ans+=pos[i]*2
if neg and pos:
    ans-=max(abs(neg[0]),abs(pos[0]))#마지막은 안 돌아와도되니까 가장 긴 걸 채택해서 빼준다.
elif pos:
    ans-=pos[0]#여길 -1로 했다가 틀렸었다
else:
    ans-=abs(neg[0])
print(ans)
#이 문제 푸느라 꽤나 고생했다.
