n=list(map(int,input().split()))
n.sort()
n1=n[0]
n2=n[1]
n3=n[2]
n4=n[3]
n5=n[4]
n=3
count=0
while count<3:
    count=0
    n+=1
    if n%n1==0:
        count+=1
    if n%n2==0:
        count+=1
    if n%n3==0:
        count+=1

    if n%n4==0:
        count+=1
    
    if n%n5==0:
        count+=1
    
    
    
print(n)


    
