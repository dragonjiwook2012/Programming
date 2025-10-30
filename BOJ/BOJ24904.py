t=input()
l=len(t)//5
for i in range(l):
    T=t[i*5:i*5+5]
    if('P' in T) and (T[0]=='C') and (T[2]=="U")and ('A' not in T) and ('B' not in T) and ('E' not in T) and ('R' not in T) and('I' not in T) and('H' not in T) and('Y' not in T) and('Z' not in T):
        print(T)
#C0U00   P
#단어 목록을 다 복사한다음 붙여넣으면 답이 나온다
#실제 사용한 코드다
#이 당시에는 CLUMP였는데
#4번만에 통과했다
#https://upload.acmicpc.net/b1232df1-45d0-48e5-9129-82f0f16a9e95/
#여기서 단어의 목록을 모두 구할 수 있다.
