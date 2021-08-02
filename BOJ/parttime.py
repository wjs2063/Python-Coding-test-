import sys
number=int(input())
a=list(map(int,input().split()))


seat=[]

for i in range(100):
    seat.append(0)

count=0

for i in range(number):
    print(a)
    n=a.pop(0)
    if seat[n-1]==1:
        count+=1
        continue
    else :
        seat[n-1]=1
print(count)
