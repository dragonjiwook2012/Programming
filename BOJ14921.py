n=int(input())
l=list(map(int,input().split()))
s,e=0,n-1
best=float('inf')
while s<e:
    if(abs(l[s]+l[e])<abs(best)):
        best=l[s]+l[e]
    if(l[s]+l[e]<0):
        s+=1
        if(s>=e):
            break
    else:
        e-=1
print(best)
#용액 합성하기
#골드 5
#전형적인 투 포인터문제
