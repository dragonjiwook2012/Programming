n = int(input())#총 페이지 수
s = str(n)
l = len(s)#길이
c = [0]*10#답 리스트
for y in range(1, l+1):#자리수 별로 확인
    k = int(s[l-y])#그 자리의 수
    left = int(s[:l-y]) if y != l else 0#그 왼쪽 수들
    right = int(s[l-y+1:]) if y != 1 else 0#그 오른쪽 수들
    for i in range(10):#0~9에서 확인
        if i == 0:#만일 0이고
            if left != 0:#0이 맨 왼쪽이 아니라면
                c[i] += (left - 1) * (10**(y-1))#일단 앞쪽 수에 대한 수를 더하고
                if k == 0:#만일 그 자리의 수가 0이라면
                    c[i] += right + 1#오른쪽걸 더함
                else:
                    c[i] += 10**(y-1)#아니라면 그냥 뒤쪽에 대한 수를 더함
        else:#아닐때
            c[i] += left * (10**(y-1))#일단 앞쪽 수에 대한 수를 더하고
            if k > i:#같지 않으면
                c[i] += 10**(y-1)#똑같이 뒤쪽에 대한 수를 더함
            elif k == i:#같을때는
                c[i] += right + 1#오른쪽걸 더함
print(*c)
#책 페이지
#Platinum.5
#솔직히 앞번호 문제 중 하나라서 옛날부터 풀고 싶었는데, 드디어 풀었다.
