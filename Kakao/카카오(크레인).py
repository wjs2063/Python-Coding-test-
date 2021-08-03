import numpy as np

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board,moves):
    board=np.array(board,dtype=int)
    height=board.shape[0]
    width=board.shape[1]
    answer=[]
    count=0
    for mv in moves:
        
        for i in range(height):
            if board[i][mv-1]>0:
                answer.append(board[i][mv-1])
                board[i][mv-1]=0
                break
        if len(answer)>1:
            if answer[-1]==answer[-2]:
                answer.pop(-1)
                answer.pop(-1)
                count+=2
            
                    
    return count

print(solution(board,moves))
