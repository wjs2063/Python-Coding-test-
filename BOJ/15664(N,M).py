N,M=map(int,input().split())
sequence=list(map(int,input().split()))
used=dict()
result=[]
sequence.sort()
def backtrack(x,n):
    if x>=M:
        s="".join(map(str,result))
        if s not in used:
            used[s]=0
            print(*result)
        return
    for i in range(n,N):
        result.append(sequence[i])
        backtrack(x+1,i+1)
        result.pop()
backtrack(0,0)
