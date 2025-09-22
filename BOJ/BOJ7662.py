import sys,heapq
input=sys.stdin.readline
t=int(input().rstrip())
def delete_min():
    while min_heap:
        _,val=heapq.heappop(min_heap)
        if(c[val]>0)#만일 사라지지 않았다면
            c[val]-=1#카운터값 1 감소
            break
def delete_max():
    while max_heap:
        _,val=heapq.heappop(max_heap)
        if(c[val]>0):#만일 사라지지 않았다며
            c[val]-=1#카운터값 1 감소
            break
def dict_to_list(dic):
    l=[]
    for key,val in dic.items():
        if(val>0):
            l.extend([key]*val)#필요가 있을지는 모르겠다...
    return l
for _ in range(t):
    k=int(input().rstrip())
    c=dict()
    min_heap=[]
    max_heap=[]
    for _ in range(k):
        command,i=input().rstrip().split()
        i=int(i)
        if(command=='I'):
            heapq.heappush(min_heap,(i,i))
            heapq.heappush(max_heap,(-i,i))
            if(i in c):
                c[i]+=1
            else:
                c[i]=1
        if(command=='D'):
            if(i==-1):
                delete_min()
            if(i==1):
                delete_max()
    li=dict_to_list(c)
    if(li):
        print(max(li),min(li))
    else:
        print('EMPTY')
#백준 7662
#이중 우선순위 


