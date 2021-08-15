x1,y1,x2,y2=map(int,input().split())
dx=x2-x1
dy=y2-y1
if dx*dy%5==0:
    print(dx*dy//5)
else:
    print(dx*dy//5+1)