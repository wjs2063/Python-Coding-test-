row,column=map(int,input().split())
box=[]
for _ in range(row):
    box.append(list(map(int,input())))

def solution():
    x,y=0,0
    max_length=0
    max_len=max(row,column)
    for length in range(max_len):
        for i in range(row):
            for j in range(column):
                x1,y1=i,j
                x2,y2=i,j+length
                x3,y3=i+length,j+length
                x4,y4=i+length,j
                if y3>=column or x3>=row:
                    continue
                if box[x1][y1]==box[x2][y2]==box[x3][y3]==box[x4][y4]:
                    max_length=max(max_length,length)
    return (max_length+1)**2
print(solution())
                
        