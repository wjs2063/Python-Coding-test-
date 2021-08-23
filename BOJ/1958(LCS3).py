import sys
input=sys.stdin.readline
a=input().strip()
b=input().strip()
c=input().strip()
dp=[[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

def lcs():

    for x in range(1,len(a)+1):
        for y in range(1,len(b)+1):
            for z in range(1,len(c)+1):
                if a[x-1]==b[y-1]==c[z-1]:
                    dp[x][y][z]=dp[x-1][y-1][z-1]+1
                else :
                    dp[x][y][z]=max(dp[x-1][y][z],dp[x][y-1][z],dp[x][y][z-1])
    return dp
dp=lcs()
for x in range(1,len(a)+1):
    for y in range(1,len(b)+1):
        m=max(dp[x][y])
print(m)
