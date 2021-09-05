from collections import deque
import sys
input=sys.stdin.readline
r,c=map(int,input().split())
graph=[]
for _ in range(r):
    a=list(input())
    graph.append(a)
visited=[[False]*c for _ in range(r)]
result=1

def dfs(x,y):
    global result
    queue=set()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue.add((x,y,graph[x][y]))
    while queue:
        x,y,z=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and (graph[nx][ny] not in z):
                queue.add((nx,ny,z+graph[nx][ny]))
                result=max(result,len(z)+1)
dfs(0,0)
print(result)


