n=int(input())
l=[]
for _ in range(n):
    t=list(input().split())
    l.append((t[0],int(t[1]),int(t[2])))
ans=0
for i in range(123,1000):
    if(str(i)[0]!=str(i)[1] and str(i)[0]!=str(i)[2] and str(i)[1]!=str(i)[2] and not '0' in list(str(i))):#i가 지켜야 할 조건
        okay=True
        i=str(i)
        for t in l:#각 결과마다 확인
            s,b=0,0
            if(t[0][0]==i[0]):#스트라이크
                s+=1
            elif(i[0] in list(t[0])):#볼
                b+=1
            if(t[0][1]==i[1]):
                s+=1
            elif(i[1] in list(t[0])):
                b+=1
            if(t[0][2]==i[2]):
                s+=1
            elif(i[2] in list(t[0])):
                b+=1
            if(s!=t[1] or b!=t[2]):#만일 값이 같지 않다면
                okay=False#실패!
                break
        if(okay):
            ans+=1
print(ans)
#실버 3
#숫자 야구
#코드가 좀 더러운 것 같으니 다음엔 좀 더 깔끔하게 짜야겠다.
