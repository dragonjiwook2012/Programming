a,b=input(),input()
al,bl=list(a)[::-1],list(b)[::-1]
ansl=[]
add=0
for i in range(max(len(al),len(bl))):
    av,bv=0,0
    if(i<len(al)):av=int(al[i])
    if(i<len(bl)):bv=int(bl[i])
    s=av+bv+add
    if(s>=10):
        add=1
        s=s%10
    else:
        add=0
    ansl.append(str(s))
if(add==1):ansl.append('1')
print("".join(ansl[::-1]))
#재밌는 문제였다.
#한칸 한칸씩 자른 뒤에 올림도 넣고 하다보니 성공했다.
#사실 파이썬은 그냥 input() 받은 다음 더해도 상관 없기는...하다
#큰 수 덧셈
