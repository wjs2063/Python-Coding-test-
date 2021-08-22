N,M=map(int,input().split())
result=[]
arr=[i for i in range(1,N+1)]
used=[False]*N

def backtrack(x,M):

    if x>=M:
        print(*result)
        return
    for i in range(len(arr)):
        if len(result)>0:
            if result[-1]>arr[i]:
                continue

        result.append(arr[i])
        backtrack(x+1,M)
        result.pop()
        
backtrack(0,M)