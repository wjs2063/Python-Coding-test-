

grid=["SL","LR"]
def solution(grid):
    answer = []
    # 북 동 남 서 순서
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    direction=[0,1,2,3]
    c_d=['U','R','D','L']
    r=len(grid)
    c=len(grid[0])
    road=[]

    for d in direction:
        my_pass=''
        first_d=d
        nx,ny=0,0
        cnt=0
        visited=[]
        while True:
            
            #S,L,R
            #벗어났을때
            if nx==0 and ny==0 and first_d==d and len(my_pass)>0:
                
                break
            if nx<0:
                nx=r-1
                continue
            if nx>=r:
                nx=0
                continue
            if ny<0:
                ny=c-1
                continue
            if ny>=c:
                ny=0
                continue
            if grid[nx][ny]=='S':

                my_pass+='S'+str(c_d[d])
                nx+=dx[d]
                ny+=dy[d]
                
                cnt+=1
                continue
            if grid[nx][ny]=='L':
                my_pass+='L'+str(c_d[d])
                d=(d-1)%4
                nx+=dx[d]
                ny+=dy[d]
                
                cnt+=1
                continue
            if grid[nx][ny]=='R':
                my_pass+='R'+str(c_d[d])
                d=(d+1)%4
                nx+=dx[d]
                ny+=dy[d]
                
                cnt+=1
                continue
        print(my_pass)


        if my_pass[2:] in road:
            continue
        road.append(my_pass)
        answer.append(cnt)      
            
    return answer
print(solution(grid))