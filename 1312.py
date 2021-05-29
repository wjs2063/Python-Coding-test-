
A,B,N=map(int,input().split())


a=[]
count=0
rest=A%B*10
while True:
    if count==N:
        break
    
    if B>rest:
        a.append(0)
        rest*=10
        count+=1
        continue
    A=rest//B
    a.append(A)
    rest=rest%B*10
    count+=1
    

print(a[N-1])




    
    

    