import math
n=int(input())
prime=[1]*(n+1)
prime[0]=0
prime[1]=0
primes=[]
for i in range(2,int(math.sqrt(n)+1)):
    if(prime[i]==1):
        for j in range(i*2,n+1,i):
            prime[j]=0
for i in range(2,n+1):
    if(prime[i]==1):
        primes.append(i)#에라토스테네스의 체
s,e=0,0#포인터
count=0#답
cur_sum=0
while True:
    if(cur_sum>=n):
        if(cur_sum==n):#만일 지금 답이라면
            count+=1#카운트 1 증가
        cur_sum-=primes[s]#시작 포인터 한칸 앞당기기
        s+=1
    elif e==len(primes):#끝 포인터가 마지막까지 도달했으면
        break#끝내기
    else:#만약 지금 합이 원하는 합보다 작으면
        cur_sum+=primes[e]#끝 포인터 한칸 증가
        e+=1
print(count)
#백준 1644
#소수의 연속합
