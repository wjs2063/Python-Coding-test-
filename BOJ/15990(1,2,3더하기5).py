from collections import deque
import sys
input=sys.stdin.readline
T=int(input())
dp=[[0]*(100000+1) for _ in range(4)]
dp[1][1]=1
dp[2][2]=1
dp[1][3]=1
dp[2][3]=1
dp[3][3]=1
for i in range(4,100000+1):
    dp[2][i]=(dp[1][i-2]+dp[3][i-2])%1000000009
    dp[1][i]=(dp[2][i-1]+dp[3][i-1])%1000000009
    dp[3][i]=(dp[1][i-3]+dp[2][i-3])%1000000009
for _ in range(T):
    n=int(input())
    
    # 4부터 해야하는 이유는 3까지는 이미 저장완료
    result=dp[1][n]+dp[2][n]+dp[3][n]
    print(result%1000000009)
    
