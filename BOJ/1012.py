t=int(input())

def connected(bat,went,column,row,green_number,i,j):
    
    q=[]
    
    if bat[i][j]==1 and (went[i][j]==False):
        q.append([i,j])
        
    count=0
    if bat[i][j]==0 :
        return 0
    
    while len(q)!=0:
        
        went[i][j]=True
        i,j=q[len(q)-1][0],q[len(q)-1][1]
        count=1
        # right
        if bat[i][j+1]==1 and (not went[i][j+1]) and j<(column-1):
            
            j+=1
            q.append([i,j])
            continue
           
        # left
        elif bat[i][j-1]==1 and (not went[i][j-1]) and j>0:
            
            j-=1
            q.append([i,j])
            continue    
        # down
        elif bat[i+1][j]==1 and (not went[i+1][j]) and i<(row-1):
            
            i+=1
            q.append([i,j])
            continue
    
        # up
        elif bat[i-1][j]==1 and (not went[i-1][j]) and i>0:
           
            i-=1
            q.append([i,j])
            continue
        i,j=q.pop()        
    return count

for _ in range(t):
    row,column,green_number=map(int,input().split())
    bat=[ [ 0 for _ in range(column+1)] for _ in range(row+1)]
    went=[[ False for _ in range(column+1)]for _ in range(row+1)]
    count=0
    
    for i in range(green_number):
        a,b=map(int,input().split())
        bat[a][b]=1
    for i in range(row):
        for j in range(column):
            if went[i][j]==True:
                continue
            else:
                n=connected(bat,went,column,row,green_number,i,j)
            count+=n 
    print(count)
         
            
    
    
    


        

            

    

    
        

        



