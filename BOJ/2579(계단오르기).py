n=int(input())
step=[0]
for _ in range(n):
    step.append(int(input()))
dp=[[0,0] for _ in range(n+1)]
def stairs(n,step):
    global dp
    if n==1:
        return step[1]
    if n==2:
        return step[1]+step[2]
    dp[1][0]=step[1]
    dp[2][0]=step[1]+step[2]
    dp[2][1]=step[2]
    #dp[x][y]:= x번째 계단까지 올랐을때의 최대점수 (x번째 단계 바로직전 오른 계단의 개수)
    #y=0 이라면 1칸오른경우이므로 그전에 반드시 2칸을올라와야함
    # y=1 이라면 2칸오른경우이므로 그전에 1칸,2칸이던 상관이없음 -> max 로 대체
    for i in range(3,n+1):
        dp[i][0]=dp[i-1][1]+step[i]
        dp[i][1]=max(dp[i-2][0],dp[i-2][1])+step[i]
    return max(dp[n][0],dp[n][1])
print(stairs(n,step))




