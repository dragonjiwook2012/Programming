n=int(input())
l=list(map(int,input().split()))
l.sort()
best=float('inf')
s,e=0,n-1
ans=(l[s],l[e])
while s<e:
    total=l[s]+l[e]
    if(abs(total)<abs(best)):
        best=total
        ans=(l[s],l[e])
    if(total>0):
        e-=1
    elif total<0:
        s+=1
    else:
        break
print(ans[0],ans[1])
#백준 2470
#두 용액
