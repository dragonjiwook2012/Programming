def solution(brown, yellow):
    l=brown//2-2
    for i in range(1,l//2+1):
        if(yellow%i==0 and i+yellow//i==l):
            return [l-i+2,i+2]
#카펫 Lv.2
#간만에 푼 프로그래머스 문제였다.
