n=int(input())
s=set()
ns=set()
for i in range(n):
    if(s):
        for k in s:
            ns.add(int(str(k)+'2'))
            ns.add(int(str(k)+'0'))
            ns.add(int(str(k)+'1'))#처음엔 이렇게 풀기 시작했지만
    else:
        ns.add(1)
        ns.add(2)
    s=ns
    ns=set()
count=0
for i in s:
    if(i%3==0) and len(str(i))==n:
        count+=1
print(count)
#각종 테케들을 넣다보니 
#1 2 3 4  5
#0 2 6 18 54   처럼 3씩 곱해져서 Large 문제에서는
n=int(input())
if(n==1):
    print(0)
else:
    print((2*(3**(n-2)))%1000000009)#처럼 풀었다.
 
