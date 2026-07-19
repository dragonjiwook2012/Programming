n=int(input())
stack=[]
def push(num):
    stack.append(num)
def spop():
    if(stack):
        stack.pop()
def top():
    if(stack):
        print(stack[-1])
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if(len(stack)==0):
        print("true")
    else:
        print("false")
for _ in range(n):
    cmd=input()
    if(cmd[:2]=="pu"):
        num=int(cmd[6:].rstrip(")"))
        push(num)
    elif(cmd[:2]=="po"):
        spop()
    elif(cmd[:2]=="to"):
        top()
    elif(cmd[:2]=="si"):
        size()
    elif(cmd[:2]=="em"):
        empty()
#전형적인 자료구조형 문제.
#원래부터 이런 류를 많이 풀어봐서 나름대로 쉬웠다.
#STL Stack
