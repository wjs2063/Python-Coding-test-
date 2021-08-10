n=int(input())
triangle=[[]]
for _ in range(n):
    triangle.append(list(map(int,input().split())))
dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
#풀이 설명
# dp[n][k]:= n번째 Level 에서 k번째 index 에 도달했을때의 최댓값
# dp[n][k]=max(dp[n-1][k-1],dp[n-1][k])+triangle 이 된다.
# 양 끝값 예외처리만 해준다면 문제없이 나옴 
def maximum_tree(n,traingle):
    if n==1:
        return triangle[1][0]
    dp[1][0]=triangle[1][0]
    for i in range(2,n+1):
        for j in range(i):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
                continue
            if j==i-1:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                continue
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+traingle[i][j]
    return max(dp[n])

print(maximum_tree(n,triangle))
            
