n,r=map(int,input().split())
ans=1
for i in range(r+1,n+1):
    ans*=i
for i in range(1,n-r+1):
    ans//=i
print(ans%100000007)
#nCr은 n!/r!/(n-r)!인데 처음엔 n! 구하고 r!으로 나눈 뒤 (n-r)로 나눴는데, 숫자가 너무 커서 에러가 나서
#그냥 n~r+1만 곱하고 1~n-r로 나눠 성공했다.
#nCr
