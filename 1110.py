number=int(input())
# number==0 이면 just cycle=0
if number<10:
    number=str(number)
    number=number.zfill(2)
else :
    number=str(number)
cycle=0


newnumber=number[:]
while True:
    

    leftnumber=str(int(newnumber[0])+int(newnumber[1]))
    newnumber=newnumber[-1]+leftnumber[-1]
    
    cycle+=1
    if number==newnumber:
        break

print(cycle)

