a,b=input(),input()
is_minus=False
if(a[0]=="-"):
    a=a[1:]
    is_minus=not is_minus
if(b[0]=="-"):
    b=b[1:]
    is_minus=not is_minus
def mult():
    ansl=[]
    for i in bl:
        l=[]
        for j in al:
            l.append(i*j)
        ansl.append(l)
    return ansl
def add_to_ans():
    ans=""
    add=0
    for i in range(len(ansl[0])-1,-1,-1):
        s=0
        for j in range(ansl_len):
            s+=ansl[j][i]
        s+=add
        if(s>=10):
            add=s//10
            s=s%10
        else:
            add=0
        ans=str(s)+ans
    ans=(str(add)+ans)
    return ans
def edit(ans):
    ans=ans[:-1].lstrip("0")
    if(is_minus):
        ans='-'+ans
    return ans
if(a=="0" or b=="0"):
    print(0)
else:
    al,bl=list(map(int,list(a))),list(map(int,list(b)))
    ansl=mult()
    ansl_len=len(ansl)
    for i in range(ansl_len):
        ansl[i]=[0]*i+ansl[i]+[0]*(ansl_len-i)
    ans=add_to_ans()
    print(edit(ans))
#역대급으로 힘들었다...
#큰 수 덧셈 느낌이기는...한데 둘째 수의 각 자리마다 첫째 수를 하나씩 곱하고 자릿수도 넣은 뒤에 다 더하면..끝이긴 하다.
#큰 수 곱셈
