from collections import deque
row,column,k=map(int,input().split())
graph=[[0]*(column+1) for _ in range(row+1)]
for _ in range(k):
    x,y=map(int,input().split())
    graph[x][y]=1

def bfs(x,y):
    cnt=0
    queue=deque([(x,y)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x,y=queue.popleft()
        if graph[x][y]!=0:
            graph[x][y]=0
            cnt+=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<=row and 0<=ny<=column and graph[nx][ny]!=0:
                    queue.append((nx,ny))
    return cnt
result=0
for x in range(1,row+1):
    for y in range(1,column+1):
        if graph[x][y]!=0:
            r=bfs(x,y)
            if r>result:
                result=r
print(result)

                





