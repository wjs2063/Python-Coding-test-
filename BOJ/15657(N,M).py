N,M=map(int,input().split())
sequence=list(map(int,input().split()))
result=[]
sequence.sort()
def back(x,n,M):
    if x>=M:
        print(*result)
        return
    for i in range(n,N):
        result.append(sequence[i])
        back(x+1,i,M)
        result.pop()
back(0,0,M)
