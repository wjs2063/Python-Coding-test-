n=437674
k=3
#조건에 맞는 소수판단 함수 필요
from collections import deque
def k_th(n,k):
    strs=""
    while n!=0:
        n,r=divmod(n,k)
        strs+=str(r)
    return strs[::-1]
def isprime(p):
    if p<=1:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
        
def solution(n,k):
    # str 형
    k_ord=k_th(n,k)

    # 1번 케이스 0이 2개인곳을  찾아보자
    left,right=0,0
    cnt=0
    # case 1
    while left<len(k_ord) and right<len(k_ord):
        
        if k_ord[left]!='0':
            left+=1
            continue
        right=left+1
        while right<len(k_ord):
            if k_ord[right]=='0':
                break
            right+=1
        # left,right 사이에 수가있다면 소수인지 체크후 개수 추가
        if len(k_ord[left:right+1])>=3:
            p=int(k_ord[left+1:right])
            if isprime(p) and '0' not in k_ord[left+1:right]:
                if right>=len(k_ord):
                    break
                cnt+=1
        # 갱신후 다시반복
        left,right=right,right+1
    # case 2
    for i in range(1,len(k_ord)):
        if k_ord[i]=='0' and '0' not in k_ord[:i] and isprime(int(k_ord[:i])):
            
            cnt+=1
    # case 3
    for i in range(len(k_ord)-1):
        if k_ord[i]=='0' and '0' not in k_ord[i+1:] and isprime(int(k_ord[i+1:])):
            
            cnt+=1
            
    if isprime(int(k_ord)) and '0' not in k_ord:
        cnt+=1
    return cnt
print(solution(n,k))
    






