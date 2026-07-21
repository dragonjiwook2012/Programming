from collections import deque
limit=2**64
n=int(input())
ans=[]
def bfs():
    q=deque([("1",1%n)])
    while q:
        s,l=q.popleft()
        if(l==0):
            ans.append(int(s))
        elif int(s)*10<=limit:
            q.append((s+"1",(l*10+1)%n))
            q.append((s+"0",(l*10)%n))
bfs()
if(ans):
    print(min(ans))
else:
    print(0)
#생각보다? 어려웠다.
#배수 (Hard)
