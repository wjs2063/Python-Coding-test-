num=int(input())

dp=[0 for _ in range(num+1)]
# dp 정의 dp[x]: x를 만들기위해 필요한 최소연산 횟수
# dp[x]=dp[x//3]+1
# dp[x]=dp[x//2]+1
# dp[x]=dp[x-1]+1 중 작은값
for i in range(2,num+1):
    # 2부터 시작이유 dp[1]=0 임 그냥 
    dp[i]=dp[i-1]+1
    # 일단은 가장 기본적인 +1 해준다
    # 그리고 그전 단계와 비교해서 전단계+1 이 더 작은값이면 넣어주자
    if i%2==0 and dp[i//2]+1<dp[i]:
        dp[i]=dp[i//2]+1
    if i%3==0 and dp[i//3]+1<dp[i]:
        dp[i]=dp[i//3]+1
print(dp[num])
    