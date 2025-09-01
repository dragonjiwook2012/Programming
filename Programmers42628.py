def solution(operations):
    import heapq
    min_heap=[]
    max_heap=[]
    for ope in operations:
        ope=list(ope.split())
        if(ope[0]=='I'):
            heapq.heappush(min_heap,int(ope[1]))
            heapq.heappush(max_heap,(-int(ope[1]),int(ope[1])))
        if(ope[0]=='D' and min_heap and max_heap):
            if(ope[1]=='-1'):
                min_target=heapq.heappop(min_heap)
                max_heap.remove((-min_target,min_target))
            else:
                max_target=heapq.heappop(max_heap)
                min_heap.remove(max_target[1])
    if(min_heap):
        min_val=heapq.heappop(min_heap)
        max_val=heapq.heappop(max_heap)[1]
        return [max_val,min_val]
    else:
        return [0,0]                       
#https://school.programmers.co.kr/learn/courses/30/lessons/42628
#이중우선순위큐
