from itertools import permutations as perm
def isPrime(n):
    if(n==0 or n==1):
        return False
    if(n==2 or n==3):
        return True
    if(n%2==0):
        return False
    for i in range(3,int(n*0.5)+1,2):
        if(n%i==0):
            return False
    return True
def solution(numbers):
    n=list(map(int,list(numbers)))
    l=set()
    for i in range(1,len(n)+1):#각 자리수마다
        for p in perm(numbers,i):#각 숫자 조합
            num=int(''.join(p))
            if(isPrime(num)):#소수라면
                l.add(num)#set에 추가
    return len(l)
https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
