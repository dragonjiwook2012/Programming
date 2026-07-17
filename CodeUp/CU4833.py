t=input()
l=len(t)
ans=0
stack=[]
for i in range(l):
    if(t[i]=="("):
        if(t[i+1]==")"):
            ans+=len(stack)
        else:
            stack.append(i)
            ans+=1
    else:
        if(t[i-1]!="("):
            stack.pop()
print(ans)
#나름대로 간단했다.
#스택 형태로 하나씩 글자를 받아오고 ()면 잘리니 ans+=1,( 바로 뒤에 )가 없는거면 이제 스택에서 하나를 지운다.
#뭐 대충 이런 느낌
#쇠 막대기
