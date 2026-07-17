b=[list(map(int,input().split())) for _ in range(19)]
def check(b):
    dx,dy=[1,0,1,1],[0,1,1,-1]
    for x in range(19):
        for y in range(19):
            if(b[y][x]==0):continue
            for i in range(3):
                if(x<=19-dx[i]*5 and y<=19-dy[i]*5):
                    r=True
                    for j in range(1,5):
                        if(b[y][x]!=b[y+dy[i]*j][x+dx[i]*j]):
                            r=False
                            break
                    if(x<=19-dx[i]*6 and y<=19-dy[i]*6 and b[y][x]==b[y+dy[i]*5][x+dx[i]*5]):
                        r=False
                    if(x>=dx[i] and y>=dy[i] and b[y][x]==b[y-dy[i]][x-dx[i]]):
                        r=False
                    if(r):
                        return (b[y][x],(y+1,x+1))
            if(x<=14 and y>=4):
                    r=True
                    for j in range(1,5):
                        if(b[y][x]!=b[y+dy[3]*j][x+dx[3]*j]):
                            r=False
                            break
                    if(x<=13 and y>=5 and b[y][x]==b[y+dy[3]*5][x+dx[3]*5]):
                        r=False
                    if(x>=1 and y<=17 and b[y][x]==b[y-dy[3]][x-dx[3]]):
                        r=False
                    if(r):
                        return (b[y][x],(y+1,x+1))
    return False
r=check(b)
if(not r):
    print(0)
else:
    w,pos=r[0],r[1]
    print(w)
    print(*pos)
#역대급으로 시간을 많이 쏟았던 문제이다.
#문제 자체의 난이도는 그닥 어렵진 않지만, 진짜 단순 노가다 작업과 조금만 실수해도 망할 수 있는 점때문에 2~3번 정도 코드를 갈아엎고 성공했다.
#오목
