row,column=map(int,input().split())

A=[]
B=[]
for i in range(row):
    A.append(list(input()))
for i in range(row):
    B.append(list(input()))
# A,B 에 넣어줌

def convert(i:int,j:int):
    global A
    # 0은 1 로 바꾸고 1은 0으로 바꾸기
    for row in range(i,i+3):
        for column in range(j,j+3):
            if A[row][column]=="0":
                A[row][column]="1"
            else:
                A[row][column]="0"
            
cnt=0
# Greedy 방법으로 i,j 가 다르면 바꿔준다
for i in range(row-2):
    for j in range(column-2):
        if A[i][j]!=B[i][j]:
            convert(i,j)
            cnt+=1
if A!=B:
    print(-1)
else:
    print(cnt)


    
