from itertools import combinations as com
n,m=map(int,input().split())
l=sorted(list(input().split()))#정렬
vowels=['a','e','i','o','u']#모음
for comb in com(l,n):#모든 조합마다
    v_count=sum(1 for ch in comb if ch in vowels)#모음의 개수와
    c_count=n-v_count#자음의 개수를 구한다음에
    if(v_count>=1 and c_count>=2):#조건을 만족하면
        print(''.join(comb))#출력하기
#백준 1759
#암호만들기
#골드 5
#브루트포스
