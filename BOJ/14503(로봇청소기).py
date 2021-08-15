from collections import deque
row,column=map(int,input().split())
x,y,direction=map(int,input().split())
room=[]
for _ in range(row):
    room.append(list(map(int,input().split())))
def turn_left():
    global direction
    direction-=1
    direction%=4
def bfs(x,y):
    cnt=1
    visited=[(x,y)]
    
    #상 우 하 좌
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    turn_time=0
    while True:
        turn_left()
        nx=x+dx[direction]
        ny=y+dy[direction]
        # 만약 방문하지않았고 뚫려있는 길이라면
        if (nx,ny) not in visited and room[nx][ny]==0:
            x=nx
            y=ny
            cnt+=1
            turn_time=0
            visited.append((x,y))
            continue
        else:
            turn_time+=1
        if turn_time==4:
            # 뒤로 후진하기
            nx=x-dx[direction]
            ny=y-dy[direction]
            if room[nx][ny]==0:
                x=nx
                y=ny
            else:
                break
            turn_time=0
    return cnt
print(bfs(x,y))


                
