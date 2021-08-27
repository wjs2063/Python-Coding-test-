n,r,c=map(int,input().split())
# 2^n x 2^n 행렬을 만듦
matrix=[[0 for _ in range(n)]for _ in range(n)]
i,j=0,0
cnt=0
# x,y 는 시작하는 좌표 
def Z(n,x,y):
    global cnt
    # 변의 길이가 2가 되면 최소 matrix
    if n==2:
        matrix[x][y]=cnt
        cnt+=1
        matrix[x][y+1]=cnt
        cnt+=1
        matrix[x+1][y]=cnt
        cnt+=1
        matrix[x+1][y+1]=cnt
        cnt+=1
        return
    Z(n//2,x,y)
    Z(n//2,x,y+n//2)
    Z(n//2,x+n//2,y)
    Z(n//2,x+n//2,y+n//2)
# 위의 함수는 오류 

def Z1(n,x,y):
    global cnt
    # 변의 길이가 2가 되면 최소 matrix
    if n==2:
        if x==r and y==c:
            print(cnt)
            return
        cnt+=1

        if x==r and y+1==c:
            print(cnt)
            return
        cnt+=1

        if x+1==r and y==c:
            print(cnt)
            return
        cnt+=1

        if x+1==r and y+1==c:
            print(cnt)
            return
        cnt+=1
        return
    Z1(n//2,x,y)
    Z1(n//2,x,y+n//2)
    Z1(n//2,x+n//2,y)
    Z1(n//2,x+n//2,y+n//2)
Z1(2**n,0,0)
result=0
while n>0:
    s=(2**n)//2
    # n=2 일때
    if n>1:
        
        if r<s and c>=s:
            result+=s**2
            c-=s
        elif r>=s and c<s:
            result+=2*s**2
            r-=s
        elif r>=s and c>=s:
            result+=3*s**2
            r-=s
            c-=s
    elif n==1:
        if r==0 and c==1:
            result+=1
        elif r==1 and c==0:
            result+=2
        elif r==1 and c==1:
            result+=3
    n-=1
print(result)



        
                
    





