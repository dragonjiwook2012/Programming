from collections import Counter
t=input()
n=len(t)
c=Counter(list(t))
ans=0
def dfs(prev,depth):#대충 문자열 만드는 dfs
    global ans
    if(depth==n):
        ans+=1
        return
    for ch in c:
        if(c[ch]>0 and ch!=prev):#전 글자와 달라야함
            c[ch]-=1
            dfs(ch,depth+1)
            c[ch]+=1
dfs("",0)
print(ans)
#실버 1
#행운의 문자열
#생각보다? 안 어려웠던 문제
