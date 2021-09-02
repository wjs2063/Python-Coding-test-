from collections import deque
import sys
input=sys.stdin.readline
col,row=map(int,input().rstrip().split())
tomato=[]
be_tomato=0
queue=deque([])
for i in range(row):
    a=list(map(int,input().split()))
    tomato.append(a)
    for j in range(col):
        if a[j]==1:
            queue.append((i,j))

def bfs():
    cnt=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        cnt+=1
        #queue 에 들어있는거 다  꺼내서 
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<row and 0<=ny<col:
                    if tomato[nx][ny]==0:
                        tomato[nx][ny]=1
                        queue.append((nx,ny))
    return cnt
r=bfs()
flag=False
for i in range(row):
    for j in range(col):
        if tomato[i][j]==0:
            flag=True
    if flag:
        break
if flag:
    print(-1)
else:
    print(r-1)


