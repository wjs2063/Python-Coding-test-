from math import sqrt,floor
M=int(input())
N=int(input())

def checkprime(number):
    if number==1:
        return 0
    if number==2 or number==3:
        return 1
    

        
    check=2
    while check<=sqrt(number):
        if number%check==0:
            return 0
        check+=1
    return 1



prime=[]
for i in range(M,N+1):
    if checkprime(i)==1:
        prime.append(i)
    

if len(prime)==0:
    print(-1)

else :
    print(sum(prime))
    print(prime[0])
