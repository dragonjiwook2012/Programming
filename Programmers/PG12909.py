def solution(s):
    answer = True
    openL=[]
    closeL=[]
    for a in s:
        if(a=='('):
            openL.append(a)
        else:
            if(openL):
                openL.pop()
            else:
                return False
    if(openL or closeL):
        return False
    return True
#https://school.programmers.co.kr/learn/courses/30/lessons/12909
#올바른 괄호
