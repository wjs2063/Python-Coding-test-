import sys
from collections import deque
input=sys.stdin.readline
n=int(input().strip())
district=[]
visited=[[False]*n for _ in range(n)]

# 적록색약 인경우와 아닌경우 를 tp 변수에 두었다
# bfs,deque 를 활용하여 적록색약인 경우는 R,G //B 로 나누어서 계산




for _ in range(n):
    district.append(list(input().strip()))
def bfs(v,tp='NO'):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    color=district[v[0]][v[1]]
    queue=deque([v])
    if visited[v[0]][v[1]]:
        return 0
    if tp=='YES':
        if color=='B':
            while queue:
                x,y=queue.popleft()
                if not visited[x][y] and district[x][y]=='B':
                    visited[x][y]=True
                    for i in range(4):
                        nx=x+dx[i]
                        ny=y+dy[i]
                        if nx<0 or  nx>=n or ny<0 or ny>=n :
                            continue
                        queue.append((nx,ny))

        else:
            while queue:
                x,y=queue.popleft()
                if not visited[x][y] and district[x][y] in ['R','G']:
                    visited[x][y]=True
                    for i in range(4):
                        nx=x+dx[i]
                        ny=y+dy[i]
                        if nx<0 or nx>=n or ny<0 or ny>=n :
                            continue
                        queue.append((nx,ny))

    else:
        while queue:
            x,y=queue.popleft()
            if not visited[x][y] and district[x][y]==color:
                visited[x][y]=True
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if nx<0 or  nx>=n or  ny<0 or ny>=n :
                        continue
                    queue.append((nx,ny))
    return 1
        
    


    
cnt=0
for i in range(n):
    for j in range(n):
        cnt+=bfs((i,j))
print(cnt)
visited=[[False]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        cnt+=bfs((i,j),'YES')
print(cnt)




