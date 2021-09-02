from collections import deque
n,m,h=map(int,input().split())
tomato=[]
queue=deque([])
for k in range(h):
    a=[]
    for i in range(m):
        b=list(map(int,input().split()))
        for j in range(n):
            if b[j]==1:
                queue.append((k,i,j))
        a.append(b)

    tomato.append(a)
def bfs():
    #(z,x,y) 기준 
    moves=[(0,-1,0),(0,0,1),(0,1,0),(0,0,-1),(1,0,0),(-1,0,0)]
    #최단거리
    cnt=-1
    #print(queue)
    while queue:
        cnt+=1
        for _ in range(len(queue)):
            z,x,y=queue.popleft()
            for move in moves:
                nx=x+move[1]
                nz=z+move[0]
                ny=y+move[2]
                # 0이라면 갈수있음
                if 0<=nz<h and 0<=nx<m and 0<=ny<n and tomato[nz][nx][ny]==0:
                    tomato[nz][nx][ny]=tomato[z][x][y]+1
                    queue.append((nz,nx,ny))
    #print(tomato)
    for z in tomato:
        for x in z:
            if 0 in x:
                return -1
    return cnt
print(bfs())
                
        

        





