import re
regex=r'(100+1+|01)+'
n=int(input())
for _ in range(n):
    t=input()
    print("YES" if re.fullmatch(regex,t) else "NO")
#이 문제는 그냥 날먹이라 생각한다
#정규분포식만 알면 걍 써진 패턴 그대로 베껴서 쓰면 답...
#GOLD 5
#Contact
