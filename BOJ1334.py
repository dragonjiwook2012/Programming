n=int(input())
l=(len(str(n))+1)//2
length=len(str(n))
if(str(n)=='9'*length):
    print(str(int(n)+2))
else:
    prefix=int(str(n)[:l])
    while True:
        if(length%2==0):
            candidate=str(prefix)+str(prefix)[::-1]
        else:
            candidate=str(prefix)+str(prefix)[:-1][::-1]
        if(int(candidate)>n):
            print(candidate)
            break
        prefix+=1
#백준 1334
#다음 팰린드롬수
