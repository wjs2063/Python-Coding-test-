from collections import deque
board=[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
#상하좌우

#시작좌표와 비용,방향이 모두 저장되어있어야 판단이가능하다

def solution(board):
    INF=int(1e10)
    # 다 최댓값으로 저장
    memory_board=[[INF]*len(board) for _ in range(len(board))]
    memory_board[0][0]=0
    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    direction=["U","D","L","R"]
    d={"U":0,
        "D":1,
        "L":2,
        "R":3}
    #시작좌표와 비용,방향이 모두 저장되어있어야 판단이가능하다
    def bfs(x,y,cost,dir=""):
        
        queue=deque()
        queue.append((x,y,cost,dir))

        while queue:
            
            x,y,now_cost,dir= queue.popleft()
            for i in range(4):
                # 갈수있는 후보지 선택
                cost=now_cost
                nx=x+dx[i]
                ny=y+dy[i]
                ndir=direction[i]
                # 출발지점은 건너뛰자
                if nx==0 and ny==0:
                    continue
                # 해당 index 벗어나거나 벽이라면 무시
                if nx<0 or nx>=len(board) or ny<0 or ny>=len(board) :
                    continue
                cost+=100
                # 코너비용
                s=dir+ndir # 코너인지 체크하는 변수
                if s in ['DR','LU','RD','UL','UR','LD','RU','DL']:
                    cost+=500
    
                # 가보지않았던 곳이거나 비용이 더 작은곳이라면 cost 저장
                ## 필독 등호가 없으면 반영이안되기때문에 꼭 꼭 꼭 등호를 붙이자
                if board[nx][ny]==0 and cost<=memory_board[nx][ny]:
                    print(f'이전 {memory_board[nx][ny]}보다 {nx,ny,cost,ndir}가 더저렴합니다 바꿉니다')
                    memory_board[nx][ny]=cost
                    queue.append((nx,ny,cost,ndir))

    bfs(0,0,0)


    answer=memory_board[-1][-1]
    return answer
print(solution(board))





    

