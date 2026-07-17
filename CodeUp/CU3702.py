r,c=map(int,input().split())
l=[[1 for _ in range(102)] for _ in range(102)]
for i in range(2,100):
    for j in range(1,i):
        l[j][i-j]=(l[j][i-j-1]+l[j-1][i-j])%100000000
print(l[r-1][c-1])
#그냥 파스칼의 정의 따라서... (50,50)까지 계산하고... 했더니 됐다.
#파스칼의 삼각형 2
