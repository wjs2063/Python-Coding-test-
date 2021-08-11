s1=input()
s2=input()
dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
#dp[x][y]:= s1 의 x번째 index s2의 y번쨰 index 까지의 LCS
for x in range(1,len(s1)+1):
    for y in range(1,len(s2)+1):
        if s1[x-1]==s2[y-1]:
            dp[x][y]=dp[x-1][y-1]+1
        else:
            dp[x][y]=max(dp[x-1][y],dp[x][y-1])

print(max(dp[len(s1)]))

 


