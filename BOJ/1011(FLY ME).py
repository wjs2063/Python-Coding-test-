import sys
input=sys.stdin.readline
n=int(input().strip())
INF=int(1e10)
for _ in range(n):
    x,y=map(int,input().split())
    dp=[INF for _ in range(y+1)]
    k1,k2,k3=0,1,2
    dp[x+1]=1
    dp[x]=0
    for i in range(x+2,y):
        dp[i]=min(dp[i-k1]+1,dp[i-k2]+1,dp[i-k3]+1)
        if dp[i]==dp[i-k1]:
            k=k1
        elif dp[i]==dp[i-k2]:
            k=k2
        else:
            k=k3
        k1,k2,k3=k-1,k,k+1
    print(dp[y-1]+1)



