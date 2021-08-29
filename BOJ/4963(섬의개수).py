import sys
from collections import deque
input=sys.stdin.readline
def dfs(x,y,graph):
    stack=deque([])
    stack.append((x,y))
    # 상 하 좌 우 대각선 포함
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    #width
    w=len(graph[0])
    # height
    h=len(graph)
    while stack:
        x,y=stack.pop()
        if graph[x][y]!=0:
            graph[x][y]=0
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w and graph[nx][ny]!=0:
                    stack.append((nx,ny))
    return 1





while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    cnt=0
    graph=[]
    for _ in range(h):
        a=list(map(int,input().split()))
        graph.append(a)
    for i in range(h):
        for j in range(w):
            if graph[i][j]!=0:
                cnt+=dfs(i,j,graph)
               
    
    print(cnt)

    
    


