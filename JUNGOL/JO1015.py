from collections import deque
f,b=deque(),deque()#f:다시 실행,b:실행 취소
n="http://www.acm.org/"#원래 사이트 주소
while True: 
    t=input()#명령어 입력받기
    if(t[0]=="B"):#실행취소
        if(len(b)==0):#실행취소가 불가능하면
            print("Ignored")#ignored 출력
        else:#아니면
            f.appendleft(n)#다시 실행에 추가하고
            n=b.pop()#마지막으로 방문한 사이트 반환받기
            print(n)
    if(t[0]=="F"):#다시 실행
        if(len(f)==0):#다시 실행이 불가능하면
            print("Ignored")#ignored 출력
        else:#아니면
            b.append(n)#실행 취소에 추가하고
            n=f.popleft()#다시 실행할 사이트 반환받기
            print(n)
    if(t[0]=="V"):#방문하기
        _,u=t.split()#URL을 받고
        f.clear()#다시 실행을 없애고
        b.append(n)#지금 있는 사이트를 실행 취소로 옮기고
        n=u#현재 사이트를 URL로 바꿈
        print(n)
    if(t[0]=="Q"):#그만하기
        break
#Gold.5
#브라우저
