n=int(input())
graph=[]
h=0
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
    if h<max(a):
        h=max(a)
visited=[[False]*n for _ in range(n)]
def dfs(x,y,height):
    stack=list()
    stack.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while stack:
        x,y=stack.pop()
        # 방문하지않았고 높이가 height 이하라면
        if not visited[x][y] and graph[x][y]>height:
            visited[x][y]=True
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<n and graph[nx][ny]>height:
                    stack.append((nx,ny))
    return 1

result=0
for h1 in range(h+1):
    visited=[[False]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h1 and not visited[i][j]:
                cnt+=dfs(i,j,h1)
    if result<cnt:
        result=cnt
    
print(result)





