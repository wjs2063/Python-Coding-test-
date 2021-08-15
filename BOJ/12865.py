N,K=map(int,input().split())
# index 를 맞춰주기위함
candidate=[[0,0]]
for _ in range(N):
    candidate.append(list(map(int,input().split())))
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
# dp matrix 생성
# dp[i][j]:= i개의 물건으로 무게 j만큼 담았을때 가치의 최댓값
# w,v에대하여 max(dp[i][j],dp[i-1][j-w]+v)
for i in range(1,N+1):
    for j in range(1,K+1):
        w=candidate[i][0]
        v=candidate[i][1]
        # 어떤걸 뺴고 다른것을 넣었을때 vs 원래
        print(i,j,w,v)
        if j>=w:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
        
print(dp[N][K])




