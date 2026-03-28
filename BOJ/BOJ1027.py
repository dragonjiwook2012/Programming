n=int(input())
l=list(map(int,input().split()))
max_ans=0
for i,v in enumerate(l):
    ans=0
    rs=-float('inf')#오른쪽 빌딩과의 기울기
    ls=float('inf')#왼쪽 빌딩과의 기울기
    if(i<n-1):#오른쪽에 빌딩이 있다면
        for j in range(i+1,n):#그 건물을 확인하면서
            if((l[j]-l[i])/(j-i)>rs):#기울기가 전의 기울기보다 크다면(보이면)
                rs=(l[j]-l[i])/(j-i)#기울기를 업데이트하고
                ans+=1#보이는 빌딩 수 추가
    if(i>0):#왼쪽에 빌딩이 있다면
        for j in range(i-1,-1,-1):#그 건물을 확인하면서
            if((l[j]-l[i])/(j-i)<ls):#기울기가 전의 기울기보다 작다면(보이면)
                ls=(l[j]-l[i])/(j-i)#기울기를 업데이트하고
                ans+=1#보이는 빌딩 수 추가
    max_ans=max(max_ans,ans)
print(max_ans)
#1027 고층빌딩
#Gold.4
