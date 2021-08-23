N,M=map(int,input().split())
sequence=list(map(int,input().split()))
sequence.sort()
result=[]
used=dict()


def backtrack(x,n,M):
    if x>=M:
        s=" ".join(map(str,result))
        if s not in used:
            used[s]=0
            print(s)
        return

    for i in range(n,N):
        if x==0 or result[-1]<=sequence[i]:
            result.append(sequence[i])
            backtrack(x+1,0,M)
            result.pop()
backtrack(0,0,M)