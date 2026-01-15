from collections import Counter
n=int(input())
nums=list(map(int,input().split()))
c=Counter(nums)#Counter으로 표현
ans=0
for i in c.keys():#각 값마다 확인
    c[i]-=1#일단 하나 감소시켜서 이 개수 1 감소
    find=False
    for j in c.keys():#또 다른 키 확인
        if(c[j]>0 and c.get(i-j,0)>0):#그 키 값과 i-j가 있을때
            c[j]-=1#둘다 감소시켜봄
            c[i-j]-=1
            if(c[j]>=0 and c[i-j]>=0):#둘다 아직 남아있다면
                find=True#찾은걸로 하고
                c[j]+=1#원상 복구
                c[i-j]+=1#원상복구
                break
            c[j]+=1#찾은게 아니여도 
            c[i-j]+=1#원상복구
    c[i]+=1#다시 복구
    if find: ans+=c[i]#이거 중요!!! 1만 더하면 안됨 c[i]를 더해야함
print(ans)
#골드 4
#좋다
#이건 제출 기록도 8번정도로 꽤 고전했는데,
#마지막에 시간초과를 pypy로 바꿔서 제출했더니
#성공!!
#AI의 도움 하나도 없이 해결했다!!
#솔직히 코드가 좀 난해한듯...
