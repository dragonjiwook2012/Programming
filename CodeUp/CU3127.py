l=list(input().split())
num=[]
def add():
    a,b=num.pop(),num.pop()
    num.append(a+b)
def sub():
    a,b=num.pop(),num.pop()
    num.append(b-a)
def mul():
    a,b=num.pop(),num.pop()
    num.append(a*b)
for i in l:
    if(i.isdigit()):
        num.append(int(i))
    else:
        if(i=="+"):
            add()
        elif(i=="-"):
            sub()
        else:
            mul()
print(num[-1])
#후위 연산자만 잘 이해하면..쉽다.
#수식 계산 1
