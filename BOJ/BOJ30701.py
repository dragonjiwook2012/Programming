from collections import deque
n,d=map(int,input().split())
armour=[]
enemy=[]
for _ in range(n):
    a,b=map(int,input().split())
    if(a==1):
        enemy.append(b)
    else:
        armour.append(b)
cnt=0
armour=deque(sorted(armour))
enemy=deque(sorted(enemy))#입력 처리 완료
while enemy:#적 리스트가 비어있지 않다면
    while(enemy and d>enemy[0]):#가능할때까지
        e=enemy.popleft()#적 학살
        d+=e
        cnt+=1
    if(armour):#가능하지 않으니 장비 사용
        a=armour.popleft()
        d*=a
        cnt+=1
    else:
        break
print(cnt+len(armour))#남은 장비 수와 지금까지 돌파한 방을 더해 출력

#실버 3
#돌아온 똥게임
#상당히 고전했던 문제이다
#오랫만에 Github에 문제 풀이를 올려본다.
#다음엔 Unity로 이런 똥겜 하나 만들어봐야겠다.
