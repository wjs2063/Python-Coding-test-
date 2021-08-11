from collections import deque
row,column=map(int,input().split())
maze=list()
for _ in range(row):
    maze.append(list(map(int,input())))
# 상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        #nx,ny 와 x,y 의 관계는 1칸관계
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 범위를 벗어났다면
            if nx<0 or nx>=row or ny<0 or ny>=column:
                continue
            #이동할수없는칸이라면
            if maze[nx][ny]==0:
                continue
            # 처음방문하는곳이라면?
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    return maze[row-1][column-1]
print(bfs(0,0))





