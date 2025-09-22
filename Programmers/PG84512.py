def solution(word):
    answer=0
    vowels=["A",'E','I','O','U']#모음들
    l=[781, 156, 31, 6, 1]#625+125+25+5+1,125+25+5+1,25+5+1,5+1,1
    for i,ch in enumerate(list(word)):
        answer+=vowels.index(ch)*l[i]
    return answer+len(word)#처음에는 len(word) 없이 했는데 테스트케이스마다 word의 길이만큼 답이 부족해서 더했더니 답이 되었다...
#모음 사전
#https://school.programmers.co.kr/learn/courses/30/lessons/84512
#LV.2
