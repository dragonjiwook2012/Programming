while True:
    inp = list(map(int, input().split()))
    if len(inp) == 1:
        break
    n = inp[0]
    heights = inp[1:]
    stack = []
    max_area = 0
    for i in range(n):
        while(stack and heights[stack[-1]]>heights[i]):
            h=heights[stack.pop()]
            w=i if not stack else i-stack[-1]-1
            max_area=max(max_area,w*h)
        stack.append(i)
    while stack:
        i=stack.pop()
        h=heights[i]
        w=n if not stack else n-stack[-1]-1
        max_area=max(max_area,w*h)
    print(max_area)
#어려워서 AI의 도움을 좀 받았다.
#다른 풀이(O(N^2))를 먼저 했는데 시간초과가 나서 선형탐색(현재 코드)를 사용했다.
#설명을 잘 못할 것 같아서 여기엔 주석을 못 달것 같은...
#1725번도 똑같이 풀 수 있다.
#히스토그램에서 가장 큰 직사각형
#Platinum.5
