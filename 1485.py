from math import sqrt
number=int(input())
point=[]
for i in range(4*number):
    a,b=map(int,input().split())
    point.append([a,b])

def square_length(x1,y1,x2,y2):
    length=0
    length+=(x1-x2)**2+(y1-y2)**2
    
    return length

# 두점의 길이계산 루트 계산 x 제곱으로 계산



def issquare(point,i):
    # square 인지 판단은 x1,y1을 기준으로 나머지 3점과거리계산
    # 제일 긴것이 대각선일것이고 그 대각선이 나머지 두변의 length 합
    # 루트 씌워주지않고 제곱한값을 return 하므로 
    # 대각선은=나머지 두변의 제곱의합 이면 정사각형
    # 나머지 두변의길이 같아야함
    x1,y1=point[4*i+0][0],point[4*i+0][1]
    x2,y2=point[4*i+1][0],point[4*i+1][1]
    x3,y3=point[4*i+2][0],point[4*i+2][1]
    x4,y4=point[4*i+3][0],point[4*i+3][1]

    l1=square_length(x1,y1,x2,y2)
    l2=square_length(x1,y1,x3,y3)
    l3=square_length(x1,y1,x4,y4)
    l4=square_length(x2,y2,x3,y3)
    l5=square_length(x2,y2,x4,y4)
    l6=square_length(x3,y3,x4,y4)

    diagonal=[l1,l2,l3,l4,l5,l6]

    diagonal.sort(reverse=True)
    dia1=diagonal.pop(0)
    dia2=diagonal.pop(0)
    if dia1==dia2:
        if diagonal[0]==diagonal[1] and diagonal[1]==diagonal[2] and diagonal[2]==diagonal[3]:
            return True
    return False
    
    
    


for i in range(number):
    if issquare(point,i):
        print(1)
        continue
    print(0)

