from collections import deque
n=int(input())
danger=[]
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    danger.append((x1,y1,x2,y2))
m=int(input())
death=[]
for _ in range(m):
    x1,y2,x2,y2=map(int,input().split())
    death.append((x1,y1,x2,y2))
def bfs(x,y):
    queue=deque()
    visited=[[False]*]
    queue.append((x,y))

