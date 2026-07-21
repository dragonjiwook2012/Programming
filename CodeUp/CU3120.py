a,b=map(int,input().split())
def bfs():
    u,d=[1,5,10],[-1,-5,-10]
    s=set([a])
    ns=set()
    ans=0
    while True:
        ns=set()
        for t in s:
            if(t==b):
                return ans
            elif(t>b):
                for i in d:
                    ns.add(i+t)
            else:
                for i in u:
                    ns.add(i+t)
        ans+=1
        s=ns
print(bfs())
#보이는 것 처럼 매우 간단하다.
#리모컨
