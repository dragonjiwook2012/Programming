t=list(input())
while True:
    changed=False
    for i in range(len(t)-1):
        if(t[i]==t[i+1]):
            changed=True
            if(t[i]=="a"):
                del t[i]
                t[i]="b"
            elif(t[i]=="b"):
                del t[i]
                t[i]="c"
            else:
                del t[i]
                t[i]="a"
            break
    if(not changed):
        print("".join(t))
        break
  #생각?보다는 꽤 어려웠다.
  #처음에는 t를 리스트가 아니라 완전 문자열로 하고,
  #앞부분,뒷부분 각각 슬라이싱 후 바뀐 문자열을 사이에 끼워넣었는데,
  #너무 시간 복잡도가 높은지, 시간초과가 났다.
  #원래는 1~30자라고 나와있지만, 실제 제출에서는 2000자가 나와서 시간초과가 된거 같아서
  #그냥 리스트로 교체후 더 가벼운 삭제&변경으로 통과되었다.
  #짝 맞추기
  #Gold.5
