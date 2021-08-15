from collections import deque


# 역삼각형 부분도  check
def sum_triangle(i,j,n_th):
    #i행 j열 길이 n
    result=0
    global t
    for k in range(n+1-n_th):
        for m in range(2*k+1):
            result+=t[k+i][m+j]
    return result
count=0
while True:
    triangle=deque(map(int,input().split()))
    n=triangle.popleft()
    if n==0:
        break
    
    t=[[0 for _ in range(2*n-1)] for _ in range(n)]
    for i in range(n):
        for j in range(2*i+1):
            t[i][j]=triangle.popleft()
    # 삼각형의 개수 A(n)=A(n-1)+(n^2-n)/2+2n-1 개이다
    # 변의길이
    init_value=0
    for n_th in range(1,n+1):
        for i in range(n_th):
            for j in range(0,2*n_th,2):
                r=sum_triangle(i,j,n_th)
                init_value=max(r,init_value)
    count+=1
    print(f'{count}. {init_value}')


