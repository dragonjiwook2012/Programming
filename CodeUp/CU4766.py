n=int(input())
l=list(map(int,input().split()))
l.sort()
m=int(input())
ind=0
ans=0
s=sum(l)
sl=[l[0]]
for i in range(1,n):
    sl.append(sl[-1]+l[i])
if(s<=m):
    print(l[-1])
else:
    while ind<=n-2:
        ans=l[n-2-ind]
        a=sl[n-2-ind]+ans*(ind+1)
        # print(ans,a)
        if(a<=m):
            print(ans+(m-a)//(ind+1))
            break
        ind+=1
    else:
        print(m//n)
#아이디어는 의외로 단순했다.
#신청한 예산을 정렬 후 맨 뒤에걸 상한선으로 모두 계산 후 안되면 상한선을 그 다음으로 큰 걸로 선정,
#만일 총 예산보다 적으면 어디까지 올려야 딱 예산보다 바로 밑인지를 계산 후 출력
#...생각보다 쉬웠다.
#예산
