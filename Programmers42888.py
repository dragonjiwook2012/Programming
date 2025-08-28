def solution(record):
    answer = []
    ids={}
    for command in record:
        if(command[0]!='L'):
            com,i,name=command.split()
        else:
            com,i=command.split()
        if(com=='Change' or com=='Enter'):
            ids[i]=name
    for command in record:
        if(command[0]!='L'):
            com,i,name=command.split()
        else:
            com,i=command.split()
        if(i in ids):# 안전장치
            if(com=='Enter'):
                answer.append(ids[i]+'님이 들어왔습니다.')
            elif(com=='Leave'):
                answer.append(ids[i]+'님이 나갔습니다.')
    return answer
#https://school.programmers.co.kr/learn/courses/30/lessons/42888
#오픈채팅
