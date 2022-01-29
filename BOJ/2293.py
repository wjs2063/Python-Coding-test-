import sys

n,k=map(int,sys.stdin.readline().split())
money=[]

for _ in range(n):
    money.append(int(sys.stdin.readline().strip()))

def solution(k,money):
    dp=[0 for _ in range(k+1)]
    dp[0]=1
    for coin in money:
        for i in range(coin,k+1):
            dp[i]+=dp[i-coin]
    return dp[k]
print(solution(k,money))