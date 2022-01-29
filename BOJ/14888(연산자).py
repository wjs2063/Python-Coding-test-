import sys
from itertools import permutations
from collections import deque
n=int(input())
number=list(map(int,input().split()))
opt=list(map(int,input().split()))
operation=[]
for _ in range(opt[0]):
    operation.append('+')
for _ in range(opt[1]):
    operation.append('-')
for _ in range(opt[2]):
    operation.append('*')
for _ in range(opt[3]):
    operation.append('%')

c=list(permutations(operation,n-1))
result=[]
#print(operation)
for i in range(len(c)):
    r=''
    r+=str(number[0])
    for j in range(n-1):
        r+=c[i][j]
        r+=str(number[j+1])
    m=1
    ans=int(r[0])
    while m<len(r)-1:
        if r[m]=='%':
            if ans<0:
                ans=abs(ans)//int(r[m+1])
                ans=-ans
                m+=2
                continue
            ans=ans//int(r[m+1])
            m+=2
            continue
        if r[m]=='*':
            ans=ans*int(r[m+1])
            m+=2
        elif r[m]=='-':
            ans-=int(r[m+1])
            m+=2
        else:
            ans+=int(r[m+1])
            m+=2
    result.append(ans)
print(max(result))
print(min(result))





    
    
        


