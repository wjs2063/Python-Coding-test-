T=int(input())
cars=[]
# 1e15 라서 시간,공간복잡도 터짐
# 1, 10, 25 // 100 1000 2500// 3묶음으로 나누기 
# 0원부터 100 원까지 
# dp[i]:= i원을만들때 필요한 최소동전수
for _ in range(T):
    cars.append(int(input()))
for car in cars:
    result=0
    dp=[0 for _ in range(100+1)]
    for i in range(1,100+1):
        dp[i]=dp[i-1]+1
        if i-10>=0:
            dp[i]=min(dp[i],dp[i-10]+1)
        if i-25>=0:
            dp[i]=min(dp[i],dp[i-25]+1)
    while car:
        result+=dp[car%100]
        car//=100
    print(result)


    

        
