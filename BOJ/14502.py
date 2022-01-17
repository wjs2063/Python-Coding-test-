
import sys
from itertools import combinations
from collections import deque
import copy
import heapq
n,m=map(int,sys.stdin.readline().split())
lab=[]
for _ in range(n):
    lab.append(list(map(int,sys.stdin.readline().split())))
wall=[]
virus=[]
for i in range(n):
    for j in range(m):
        if lab[i][j]==2:
            virus.append((i,j))
        if lab[i][j]==0:
            wall.append((i,j))
wall_combination=list(combinations(wall, 3))

def dfs(x,y,grp):
    
    q=deque([])
    q.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited=[[False ]*m for _ in range(n)]
    while q:
        a,b=q.popleft()
        if not visited[a][b]:
            visited[a][b]=True
            for i in range(4):
                nx=a+dx[i]
                ny=b+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m or grp[nx][ny]==1:
                    continue
                q.append((nx,ny))
                grp[nx][ny]=2
    return grp
h=[]
for w in wall_combination:
    grp=copy.deepcopy(lab)
    for w1 in w:
        grp[w1[0]][w1[1]]=1

    for v in virus:
        grp=dfs(v[0],v[1],grp)
    cnt=0
    for i in range(n):
        for j in range(m):
            if grp[i][j]==0:
                cnt+=1
    heapq.heappush(h,(-cnt,cnt))
print(heapq.heappop(h)[1])
    
    
        



        
