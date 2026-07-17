n=int(input())
l=list(map(int,input().split()))
stack=[(l[-1],n-1)]
ans=[0]*n
for i in range(n-2,-1,-1):
	while(stack and stack[-1][0]<=l[i]):
		h,ind=stack.pop()
		ans[ind]=i+1
	stack.append((l[i],i))
print(*ans)
#솔직히 처음(처음에는 한번 시간초과가 남)이랑 뭐가 달라진지는 잘 모르겠지만, 알고리즘을 다시 짜니 성공했다...
#탑
