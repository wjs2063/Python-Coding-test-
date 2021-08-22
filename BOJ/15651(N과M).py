N,M=map(int,input().split())
result=[]
arr=[i for i in range(1,N+1)]
used=[False]*N

def repeat(x,M):
    if x>=M:
        print(*result)
        return
    for i in range(len(arr)):
        result.append(arr[i])
        repeat(x+1,M)
        result.pop()
repeat(0,M)
