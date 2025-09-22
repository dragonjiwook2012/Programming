from itertools import combinations as comb
def solution(nums):
    answer = 0
    c=list(map(list,comb(nums,3)))
    for C in c:
        if(is_prime(sum(C))):answer+=1
    return answer
def is_prime(n):
    if(n==0 or n==1):return False
    elif(n==2 or n==3):return True
    elif(n%2==0):return False
    for i in range(3,round(n**0.5)+2):
        if(n%i==0):return False
    return True
#https://school.programmers.co.kr/learn/courses/30/lessons/12977
#소수만들기
