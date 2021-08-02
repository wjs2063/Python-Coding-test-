m,n=map(int,input().split())
chess=[]
for i in range(m):
    chess.append(str(input()))


def Bcountingchess(chess,m,n):
    count=0
    first=chess[m][n]
    for i in range(m,m+8):
        
        for j in range(n,n+8):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                if chess[i][j]!=first:
                    count+=1
            else :
                if chess[i][j]==first:
                    count+=1
        
                    
    return min(count,64-count)


count=[]

for i in range(m-7):
    for j in range(n-7):
        count.append(Bcountingchess(chess,i,j))
        
print(min(count))


