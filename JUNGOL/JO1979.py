import math
n1,n2,n=map(int,input().split())
l=print(math.floor(sum(sorted(list(map(int,input().split())))[n2:n-n1])/(n-n1-n2)))#뭔가 복잡해 보이지만 생각보다 쉽다.
#이게.. 실버 1? 아무리 높게 쳐줘도 실버 4 언저린거 같긴 하다.
#The Average
#Silver.1
