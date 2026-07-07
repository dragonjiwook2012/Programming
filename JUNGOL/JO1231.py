n=int(input())
l=list(input().split())
d={"010":[],"011":[],"016":[],"017":[],"018":[],"019":[]}
for _ in range(n):
    t=list(input().split("-"))
    d[t[0]].append([t[1],t[2]])
for k in d.keys():
    d[k]=sorted(d[k],key=lambda x:(-len(x[0]),x[0],x[1]))#원래 -len(x[0]) 뒤에 x[0],x[1]이 없어도 사전순 정렬을 알아서 하는 줄 알아서 몇 번 틀렸다...
for i in l:
    t="01"+i
    for x in d[t]:
        print("-".join([t]+x).rstrip())
#실버 1이라기에는 좀.. 너무 쉽다..
#휴대폰번호 정렬
#Silver.1
