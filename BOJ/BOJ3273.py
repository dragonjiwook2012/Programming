n=int(input())
l=set(list(map(int,input().split())))
x=int(input())
cnt=0
for i in l:
    if(x-i in l):
        cnt+=1
print(cnt//2)#a->b,b->a로 두 개씩 중복이 있기 때문에 2로 나눈다
#10분만에 풀었다.
#초반에 "서로 다른 수"라는 말이 나오니 Set을 사용하면 in 연산이 O(1)정도로 처리되기 때문에 이렇게 풀면 된다.
