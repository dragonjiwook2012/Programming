def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)#정렬
    while scoville:
        f=heapq.heappop(scoville)#가장 안 매운거
        if(f>=K):#가장 안매운게 K보다 맵다면
            return answer
        if not scoville:#만일 음식이 더 없다면
            return -1#종료
        s=heapq.heappop(scoville)#다음으로 안 매운거
        heapq.heappush(scoville,f+s*2)
        answer+=1#횟수 추가
    return -1
  #더 맵게
  #https://school.programmers.co.kr/learn/courses/30/lessons/42626
  #LV.2
