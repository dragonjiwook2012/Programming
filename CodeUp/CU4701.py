n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=float('inf')
idx1,idx2=-1,-1
left,right=0,n-1
while left<right:
    s=l[left]+l[right]
    if(abs(ans)>abs(s)):
        idx1,idx2=left,right
        ans=s
    if(s==0):
        break
    elif(s>0):
        right-=1
    else:
        left+=1
print(l[idx1],l[idx2])
#그냥 전형적인 투 포인터 문제다.
#두 용액
