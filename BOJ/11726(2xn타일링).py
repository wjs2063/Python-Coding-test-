n=int(input())
dp=[0 for _ in range(1001)]
dp[1],dp[2]=1,2
def tile(n):
    global dp
    if n<=2:
        return dp[n]
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%10007
# dp[n]:= 2xn 의 타일을 채우는 방법의 수 dp[n]=dp[n-1]+d[n-2]
print(tile(n))

