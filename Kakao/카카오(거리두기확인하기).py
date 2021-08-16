places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    answer=[]
    manhatten_1=[(1,0),(0,1),(-1,0),(0,-1)]
    manhatten_2=[(0,-2),(1,-1),(2,0),(1,1),(0,2),(-1,1),(-2,0),(-1,-1)]
    def too_close(p):
        
        for x in range(5):
            for y in range(5):
                if p[x][y]=='P':
                    for dx,dy in manhatten_1:
                        nx=x+dx
                        ny=y+dy
                        if nx<0 or nx>=5 or ny<0 or ny>=5:
                            continue
                        if p[nx][ny]=='P':
                            answer.append(0)
                            return False
                    for dx,dy in manhatten_2:
                        nx=x+dx
                        ny=y+dy
                        if nx<0 or nx>=5 or ny<0 or  ny>=5:
                            continue
                        if p[nx][ny]=='P':
                            if (dx,dy) in ((0,2),(-2,0),(0,-2),(2,0)):
                                dx//=2
                                dy//=2
                                nx=x+dx
                                ny=y+dy
                                if p[nx][ny]=='X':
                                    continue


                            if p[nx][y]=='X' and p[x][ny]=='X':
                                continue
                            answer.append(0)
                            return False
        answer.append(1)
        return True
    for _ in range(5):
        p=places.pop(0)
        #사람 찾기
        c=too_close(p)
                    
    return answer
print(solution(places))