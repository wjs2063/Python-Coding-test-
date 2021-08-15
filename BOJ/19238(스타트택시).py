from collections import deque
row,M,fuel=map(int,input().split())
maze=[]
for _ in range(row):
    maze.append(list(map(int,input().split())))
# 택시위치 저장
x,y=map(int,input().split())
customer=[]
# 손님위치 출발,목적지 저장
for _ in range(M):
    customer.append(list(map(int,input().split())))
##저장완료
# 상 하 좌 우 변화량 저장
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# 출발지와 가고자하는 위치까지 거리 계산하기 
def bfs(start_x,start_y,end_x,end_y,maze)->list:
    global fuel
    queue=deque()
    queue.append((start_x,start_y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 맵 바깥쪽이거나 벽or 지나갔던곳이라면
            if nx<0 or nx>=row or ny<0 or ny>=row or maze[nx][ny]>0 :
                continue
            maze[nx][ny]=maze[x][y]+1
            fuel-=1
            if nx==end_x and ny==end_y:
                fuel+=maze[nx][ny] #연료-사용연료+2*사용연료
                return True,maze[nx][ny],end_x,end_y
            if fuel==0:
                return False,-1,-1,-1
def find_customer():
    global customer
    distance=[]
    for cus in customer:
        d=bfs(x,y,cus[0],cus[1])
        # 가능한 손님을 저장하자
        if d[0]:
            distance.append(d[1:])
    # distance,index,row 순으로 정렬하자
    if distance:
        distance.sort(key=lambda x:(x[0],x[1],x[2]))
    # distance 에 아무도없다면 불가능
    else :
        return False
    return distance[0]

while True:
    a=find_customer()
    if ~a:
        print(-1)
        break
    

    







    

    
