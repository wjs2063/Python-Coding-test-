import copy
from collections import deque
N,M=map(int,input().split())
sequence=list(map(int,input().split()))
result=deque()
# 무조건 딕셔너리 사용할것. 시간초과 엄청뜬다 ㅠㅠ
used={}
u=[False]*N
sequence.sort()
def back(x,start,M):
    if x>=M:
        s="".join(map(str,result))
        if s not in used:
            used[s]=0
            print(*result)
            return
        return
    for i in range(start,N):
        if u[i]:
            continue
        u[i]=True
        result.append(sequence[i])
        back(x+1,0,M)
        result.pop()
        u[i]=False

back(0,0,M)