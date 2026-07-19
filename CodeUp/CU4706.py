n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=float('inf')
idx1,idx2,idx3=-1,-1,-1
for i in range(n-1):
    left,right=i+1,n-1
    while left<right:
        if(left!=i and right!=i):
            s=l[left]+l[right]+l[i]
            if(abs(ans)>abs(s)):
                idx1,idx2,idx3=left,right,i
                ans=s
        if(s==0):
            break
        elif(s>0):
            right-=1
        else:
            left+=1
print(*sorted([l[idx1],l[idx2],l[idx3]]))
#아까 그 두 용액 문제에 하나 더 추가하면 된다.
#생각보다 간단하다..
#세 용액
