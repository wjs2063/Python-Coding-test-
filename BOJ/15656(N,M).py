N,M=map(int,input().split())
sequence=list(map(int,input().split()))
result=[]
used=[False]*N
sequence.sort()
def back(x,M):
    if x>=M:
        print(*result)
        return
    for i in range(N):
        result.append(sequence[i])
        back(x+1,M)
        result.pop()
back(0,M)