from math import factorial
f=str(factorial(int(input())))[::-1]#팩토리얼 후 뒤집고
for k in f:#마지막 글자(지만 뒤집었으니 첫번째 글자)부터 하나하나 확인
    if(k!='0'):#만일 0이 아니면 
        print(k)#출력후
        break#break!
#실버 2여서 그런지 간단하다.
#백준 2553 마지막 팩토리얼 수
#실버 2
