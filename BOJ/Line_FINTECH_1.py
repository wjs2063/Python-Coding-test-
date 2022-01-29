record=["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
purchase=[]
sell=[]

for i in range(len(record)):
    if record[i][0]=='P':
        t=record[i].split()
        purchase.append([i,int(t[1]),int(t[2])])
    else:
        t=record[i].split()
        sell.append([i,int(t[1]),int(t[2])])
def solution(record):
    first,last=0,0
    total=0
    j=0
    for i in range(len(sell)):
        total+=sell[i][2]
        
    while total-purchase[j][2]>0:
        total-=purchase[j][2]
        first+=purchase[j][1]*purchase[j][2]
        j+=1
    first+=abs(total)*purchase[j][1]
    for i in range(len(sell)):
        n=sell[i][0]
        p=sell[i][1]
        c=sell[i][2]
        j=n-1-i
        while c-purchase[j][2]>0 and c>0:
            last+=purchase[j][1]*purchase[j][2]
            c-=purchase[j][2]
            purchase[j][2]=0
            j-=1

        last+=c*purchase[j][1]
        purchase[j][2]-=c
    return [first,last]
    

print(solution(record))