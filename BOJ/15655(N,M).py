N,M=map(int,input().split())
sequence=list(map(int,input().split()))
result=[]
used=[False]*N
sequence.sort()
def backtrack(x,M):
    if x>=M:
        print(*result)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i]=True
        result.append(sequence[i])
        backtrack(x+1,M)
        result.pop()
        for j in range(i+1,N):
            used[j]=False
backtrack(0,M)
##
#더좋은풀이
def back(n):
    if len(result) == M:
        print(*result)
        return
    for i in range(n, N):
        result.append(sequence[i])
        back(i+1)
        result.pop()
back(0)