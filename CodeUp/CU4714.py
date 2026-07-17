n,m=map(int,input().split())
prev={i:[] for i in range(1,n+1)}
subs={i:[] for i in range(1,n+1)}
ans=0
for _ in range(m):
    a,b=map(int,input().split())
    subs[a].append(b)
    prev[b].append(a)
def search(n):
    prev_c,subs_c=0,0
    v=set([n])
    s=[n]
    while s:#previous
        k=s.pop()
        v.add(k)
        for i in prev[k]:
            if(i not in v):
                v.add(i)
                s.append(i)
                prev_c+=1
    v=set([n])
    s=[n]
    while s:#subsequent
        k=s.pop()
        v.add(k)
        for i in subs[k]:
            if(i not in v):
                v.add(i)
                s.append(i)
                subs_c+=1
    return prev_c,subs_c
for i in range(1,n+1):
    pc,sc=search(i)
    if(pc+sc==n-1):
        ans+=1
print(ans)
#나쁘진... 않은 문제였다.
#키의 순서가 결정된 사람이 총 인원-1이면 그 사람의 순서가 결정된거다.
참고로 18줄, 28줄을 처음에 빼놓아서 한 번 틀렸다.
#키 순서
