n=int(input())
l=[[False]*n for _ in range(n)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    l[a-1][b-1]=True
    l[b-1][a-1]=True
def dfs():
    stack=[1]
    v=set([1])
    ans=set()
    while stack:
        c=stack.pop()
        for i in range(n):
            if (l[c-1][i] and i+1 not in v):
                stack.append(i+1)
                ans.add(i+1)
                v.add(i+1)
    return len(list(ans))
print(dfs())
#이건 2차원 상에서의 B/DFS가 아니라 그래프 상에서라서 좀 재밌었다.
#바이러스
