import sys
from collections import deque
input=sys.stdin.readline
T=int(input())

def bfs(x,y,n,e_x,e_y,graph):

    visited=[[False for _ in range(n)] for _ in range(n)]
    move=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    queue=deque([(x,y)])
    cnt=0
    while queue:
        x,y=queue.popleft()
        if not visited[x][y]:
            visited[x][y]=True
            for mv in move:
                dx,dy=mv
                nx=x+dx
                ny=y+dy
                if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]:
                    continue

                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[e_x][e_y]





for _ in range(T):
    n=int(input())
    s_x,s_y=map(int,input().split())
    e_x,e_y=map(int,input().split())
    graph=[[0 for _ in range(n)]for _ in range(n)]
    print(bfs(s_x,s_y,n,e_x,e_y,graph))
