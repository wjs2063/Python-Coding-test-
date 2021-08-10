n=int(input())
sequence=list(map(int,input().split()))
dp=[1 for _ in range(n+1)]
# 1로 초기화 하는이유는 자기자신이 수열이될수도있으니까 
# dp[n]:= n번째 원소가 last 값일때 가장 긴 증가하는 부분수열의 개수
for i in range(n):
    for j in range(i):
        if sequence[i]>sequence[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
