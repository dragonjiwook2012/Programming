n=int(input())
l=(len(str(n))+1)//2
length=len(str(n))
if(str(n)=='9'*length):#만일 9로만 이루어진 수라면
    print(str(int(n)+2))#2만 더하고 보내면 됨
else:#그게 아니면
    prefix=int(str(n)[:l])#절반으로 쪼개고
    while True:
        if(length%2==0):
            candidate=str(prefix)+str(prefix)[::-1]#prefix라는 변수를 1씩 증가시키며
        else:
            candidate=str(prefix)+str(prefix)[:-1][::-1]
        if(int(candidate)>n):#성공할때까지 반복한다
            print(candidate)
            break
        prefix+=1
#백준 1334
#다음 팰린드롬수
