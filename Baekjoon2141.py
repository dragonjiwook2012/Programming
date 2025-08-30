n=int(input())
villages=[]
for _ in range(n):
    pos,population=map(int,input().split())
    villages.append((pospopulation))
villages.sort()
total_population=sum(pop for _,pop in villages)
half_population=(total_population + 1)//2
cumulative=0
for pos,pop in villages:
    cumulative+=pop
    if cumulative>=half_population:
        print(pos)
        break
#백준 2141
#우체국
