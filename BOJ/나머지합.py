import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())

a=list(map(int,input().split()))

memo=defaultdict(int)

b=[0]+a

def h(v):
    if v==0:
        return 0
    if v==1 :
        return 1
    return (v+1)*v//2
answer=0

for i in range(1,n+1):
    b[i]+=b[i-1]
    memo[b[i]%m]+=1


# 나머지로 저장 그리고 (p[j]-p[i])mod m =0 이여야하는데 각각의 나머지가같아야함
# 단 각 나머지가 0일경우에 자기자신도가능하므로 중복조합으로 
# 1이상일경우에 콤비네이션으로 해결해준다.
answer+=h(memo[0])
for i in range(1,m):
    n=memo[i]
    answer+=n*(n-1)//2
print(answer)
