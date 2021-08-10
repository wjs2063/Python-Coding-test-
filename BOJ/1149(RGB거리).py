n=int(input())
colors=[]
for _ in range(n):
    colors.append(list(map(int,input().split())))
dp=[[0 for _ in range(3)]for _ in range(n+1)]
dp[1]=colors.pop(0)
i=2
##아이디어는 n번째 집에 어떤 color 가 칠해질것이냐?
for color in colors:
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color[0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color[1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color[2]
    i+=1
answer=min(dp[n])

print(answer)



