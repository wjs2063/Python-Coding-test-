N,M=map(int,input().split())
sequence=list(map(int,input().split()))
sequence.sort()
used=[False]*N
result=[]
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
        used[i]=False

backtrack(0,M)