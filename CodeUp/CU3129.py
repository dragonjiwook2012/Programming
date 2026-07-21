t=input()
ok=True
s,b=0,0
for i in t:
    if(i=="("):
        s+=1
    elif(i=="["):
        b+=1
    elif(i==")"):
        if(s>0):
            s-=1
        else:
            ok=False
    else:
        if(b>0):
            b-=1
        else:
            ok=False
if(ok and s==0 and b==0):
    print("good")
else:
    print("bad")
#걍 풀만 하다.
#올바른 괄호 2
