import sys
input=sys.stdin.readline
n=int(input())

grape=[-1]

for _ in range(n):
    grape.append(int(input().strip()))
dp=[0 for _ in range(n+1)]
dp[1]=grape[1]
if n>1:
    dp[2]=grape[1]+grape[2]
for i in range(3,n+1):
    dp[i]=max(dp[i-2]+grape[i],grape[i]+grape[i-1]+dp[i-3],dp[i-1])
print(dp[n])
