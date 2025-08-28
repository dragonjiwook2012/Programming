def solution(s):
    answer = len(s)
    l=len(s)
    for i in range(1,l//2+1):
        compressed=''
        count=1
        t=s[:i]
        for j in range(i,l,i):
            cur=s[j:j+i]
            if(s[j:j+i]==t):
                count+=1
            else:
                compressed+=(str(count)+t if count>1 else ""+t)
                t=cur
                count=1
        compressed+=(str(count) if count>1 else "")+t
        answer=min(answer,len(compressed))
    return answer
##https://school.programmers.co.kr/learn/courses/30/lessons/60057
##문자열압축
