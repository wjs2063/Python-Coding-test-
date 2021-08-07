from collections import deque
n=int(input())
word=list(map(str,input().split()))

dp=[[-1 for _ in range(5001)] for _ in range(5001)]
## 2차원 배열 생성
left=0
right=5000

def solution(dp,left,right):
    
    if left>right:
        return 0
    if dp[left][right]!=-1:
        return dp[left][right]
    
    if word[left]==word[right]:
        dp[left][right]=dp[left+1][right-1]
    else :
        dp[left][right]=min(dp[left][right-1]+1,dp[left+1][right]+1)
    return dp[left][right]

for i in range(n-1):
    for j in range(i+1,n):
        dp[i][j]=solution(dp,i,j)
print(dp[0][n-1])



    
    