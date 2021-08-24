from collections import deque
board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
def square(i,j,board):
    dx=[0,0,1,1]
    dy=[0,1,0,1]
    n=len(board)
    m=len(board[0])
    s=board[i][j]
    for dir in range(1,4):
        nx=i+dx[dir]
        ny=j+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            return False
        if s!=board[nx][ny] or s==0:
            return False
    return True
def down(board):
    for col in range(len(board[0])):
        queue=deque()
        for row in range(len(board)-1,-1,-1):
            if board[row][col]!=0:
                queue.append(board[row][col])
        for row in range(len(board)-1,-1,-1):
            if len(queue)!=0:
                board[row][col]=queue.popleft()
            else:
                board[row][col]=0
    return board




def solution(m,n,board):
    board=list(map(lambda x:list(x),board))
    cnt=0
    while True:
        a=[]
        
        for i in range(m):
            for j in range(n):
                if square(i,j,board):
                    a.append((i,j))

        #a 에 담겨있는 시작 i,j 에 대하여 각 2x2 인덱스값을 튜플형태로 저장후 set 의개수=block 
        s=[]
        for x,y in a:
            s.append((x,y))
            s.append((x,y+1))
            s.append((x+1,y))
            s.append((x+1,y+1))
        s=set(s)
        cnt+=len(s)
        # s에있는 tuple 형태의 좌표를 받아 0으로 만들어줌
        for x,y in s:
            board[x][y]=0
        if len(a)==0:
            break
        board=down(board)

    
    return cnt

print(solution(4,5,board))




