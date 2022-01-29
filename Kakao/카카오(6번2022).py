board=[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill=[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
import copy
def attack(board,r1,c1,r2,c2,degree,state):
    cnt=0
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            a=board[i][j]
            board[i][j]-=degree
            if a>0 and board[i][j]<=0:
                cnt+=1
    return board,cnt
def healing(board,r1,c1,r2,c2,degree,state):
    cnt=0

    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            a=board[i][j]
            board[i][j]+=degree
            if a<=0 and board[i][j]>0:
                cnt+=1
    return board,cnt

def solution(board,skill):
    n=len(board)
    m=len(board[0])
    cnt=n*m
    # 이전 state 와 같으면 0
    # 다르면 1을 return 하는 xor 연산?
    state=[[True]*m for _ in range(n)]
    for sk in skill:
        t,r1,c1,r2,c2,degree=sk
        if t==1:
            board,r=attack(board,r1,c1,r2,c2,degree,state)
            cnt-=r

        else:
            board,r=healing(board,r1,c1,r2,c2,degree,state)
            cnt+=r
    return cnt
print(solution(board,skill))
def solution(board,skill):
    n=len(board)
    m=len(board[0])
    cnt=n*m
    for sk in skill:
        t,r1,c1,r2,c2,degree=sk


    
    

def attack(board,r1,c1,r2,c2,degree):
    cnt=0
    cp=copy.copy(board)
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            board[i][j]-=degree
    return board
def healing(board,r1,c1,r2,c2,degree):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            board[i][j]+=degree

    return board
