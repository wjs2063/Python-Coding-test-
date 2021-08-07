from collections import defaultdict


n,k=map(int,input().split())
cnt=0
'''
똑같은 물병만 합칠수있으므로 1,2,4,8 . . .
예를들어 생각해보자 
15,1 이주어졌다
15를 2로나눈다 그러면 
1L:1개 2L:7개 
또반복 7을 2로나눈다
1L:1개 2L:1개 4L:3개
또 반복
1L:1개 2L:1개 4L:1개 8L:1개
2진수 표현  
'''
while bin(n).count("1")>k:
    n+=1
    cnt+=1
print(cnt)

# 나를 애먹인 문제
# 아래코드는 실행했다가 시간초과로 퇴짜맞았다..
'''
from collections import defaultdict


n,k=map(int,input().split())

def solution(n,k):
    if k>n:
        return 0
    # 1의 개수가 곧 물병의 개수 임 
    # 1의 개수 counting 해주자
    n=bin(n)[2:]
    total=0
    total=n.count("1")
    cnt=0
    while total>k:
        total=0
        cnt+=1
        n=int(n,2)+1
        n=bin(n)[2:]
        for i in range(len(n)):
            if n[i]=="1":
                total+=1
    return cnt



print(solution(n,k))





bottle=defaultdict(int)
if k>=n:
    print(0)
else:
    i=1
    while n//2>=1:
        n,rest=divmod(n,2)
        bottle[i]=rest
        bottle[2*i]=n
        i*=2

    ## 기본작업완료
    # 이제 길이가 k보다 크다면 1개씩 사서 계속반복해주기
    cnt=0
    total_bottle=sum(list(bottle.values()))
    while k<total_bottle:
        cnt+=1
        bottle[1]+=1
        bottle_k=list(bottle.keys())
        for key in bottle_k:
            #모두다 검색
            
            if bottle[key]>1:
                div,rest=divmod(bottle[key],2)
                bottle[key]=rest
                bottle[key*2]+=div
        
        total_bottle=sum(list(bottle.values()))

    print(cnt)
            


'''