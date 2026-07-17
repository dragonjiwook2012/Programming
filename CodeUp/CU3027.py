t1,t2=input(),input()

def ipt(t1,t2):
    if("+" in t1):
        a1,b=t1.split("x+")
    else:
        a1,b=t1.split("x")
    if(a1==""):a1=1
    elif(a1=="-"):a1=-1
    b1,c1=b.split("y=")
    if(b1==""):b1=1
    elif(b1=="-"):b1=-1
    a1,b1,c1=int(a1),int(b1),int(c1)
    t=t2.split("x+")
    if("+" in t2):
        a2,b=t2.split("x+")
    else:
        a2,b=t2.split("x")
    if(a2==""): a2=1
    elif(a2=="-"): a2=-1
    b2,c2=b.split("y=")
    if(b2==""):b2=1
    elif(b2=="-"):b2=-1
    a2,b2,c2=int(a2),int(b2),int(c2)
    return a1,b1,c1,a2,b2,c2
a1,b1,c1,a2,b2,c2=ipt(t1,t2)
if(b1/a1==b2/a2 and c1/a1==c2/a2):
    print("Indeterminate")
elif(b1/a1==b2/a2 and c1/a1!=c2/a2):
    print("Impossible")
else:
    tx=a1*a2
    b1*=a2
    b2*=a1
    c1*=a2
    c2*=a1
    y=(c1-c2)/(b1-b2)
    x=(c1-b1*y)/tx
    print("x = "+str(int(x)))
    print("y = "+str(int(y)))
#뭔가 굉장히 복잡해보이지만 난이도 자체는 꽤 쉽다.(그야 이 문제는 쉬운 버전이다...)
#연립방정식을 찾아라!(Easy)
