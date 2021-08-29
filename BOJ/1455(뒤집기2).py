n,m=map(int,input().split())
coin=[]
for _ in range(n):
    a=list(input())
    coin.append(list(map(int,a)))
# x,y 를 뒤집고싶다면
def convert(x,y):
    # x,y 를  convert 하고싶다면 
    # 1이면 인정사정없이 뒤집어도됨 x,y-1 x-1,y 를 뒤집어야할지생각도해봤는데 굳이?
    for i in range(x,-1,-1):
        for j in range(y,-1,-1):
            coin[i][j]=1-coin[i][j]
cnt=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if coin[i][j]==1:
            convert(i,j)
            cnt+=1
print(cnt)
