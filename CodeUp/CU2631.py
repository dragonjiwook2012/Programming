n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=0
lp,rp=0,0
s=l[0]
while lp<=rp:
    if(s<k):
        rp+=1
        if(rp>=n):
            break
        s+=l[rp]
    elif(s>=k):
        if(s==k):ans+=1
        lp+=1
        s-=l[lp-1]
print(ans)
#처음에는 모든 인덱스에서 오른쪽으로 이동하고, 그게 답과 맞는지 비교 후 답보다 크면 다음으로 넘어가는 식으로 했는데,
#그냥 투포인터가 답이였다..
#보물찾기
