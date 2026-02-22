#(100+1+|01)+
import re
print("SUBMARINE" if re.fullmatch(r'(100+1+|01)+',input()) else "NOISE")
#얘도 걍 ~을 +로 변환 후 그대로 정규분포식에 넣면 된다.
#그래도 1013번보단 좀 더 신경써서 문제를 만든 듯 하다
#GOLD 5
#잠수함 식별
