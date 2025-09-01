n=int(input())
l=list(map(int,input().split()))
l.sort()
best=float('inf')#가장 좋은 값은 일단 무한
s,e=0,n-1#맨 앞과 맨 뒤
ans=(l[s],l[e])
while s<e:
    total=l[s]+l[e]
    if(abs(total)<abs(best)):#만일 best보다 지금이 더 좋으면
        best=total
        ans=(l[s],l[e])#값 변경
    if(total>0):#만일 양수면
        e-=1#끝을 한칸 앞당기고
    elif total<0:#음수면
        s+=1#시작을 한칸 뒤로
    else:
        break#0일때는 최선으로 그냥 바로 break
print(ans[0],ans[1])
#백준 2470
#두 용액
