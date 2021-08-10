n=int(input())
test_case=[]
for _ in range(n):
    test_case.append(int(input()))

for num in test_case:
    
    dp=[0 for _ in range(15)]
    dp[1],dp[2],dp[3]=1,2,4
    
    if num>=4:
        for i in range(4,num+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[num])



