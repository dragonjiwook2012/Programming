n=int(input())
l=list(int(input()) for _ in range(n))[::-1]
stack=[(l[-1],n-1)]
ansl=[0]*n
for i in range(n-2,-1,-1):
	while(stack and stack[-1][0]<=l[i]):
		h,ind=stack.pop()
		ansl[ind]=i+1
	stack.append((l[i],i))
ansl.reverse()
ans=0
for i in range(n):
    ans+=i-ansl[i]
print(ans)
#사실 이건 탑 문제의 코드를 베낀 뒤에 살짝 수정한거다..
#꽤 재미있었다.
#소들의 헤어스타
