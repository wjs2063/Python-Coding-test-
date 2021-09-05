from collections import deque
m,n,k=map(int,input().split())

graph=[[1]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x_min,y_min,x_max,y_max=map(int,input().split())
    for i in range(x_min,x_max):
        for j in range(y_min,y_max):
            graph[i][j]=0
print(graph)
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
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=0:
                    queue.append((nx,ny))
    return cnt
result=0
rec=[]
for x in range(n):
    for y in range(m):
        if graph[x][y]!=0:
            rec.append(bfs(x,y))
            result+=1
rec.sort()
print(result)
print(*rec)
        


    