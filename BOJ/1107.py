'''
import sys
from itertools import product

N=input().strip()
n=int(sys.stdin.readline())
if n:
    brk=sys.stdin.readline().split()
else:
    brk=[]

remote=[str(i) for i in range(10) if str(i) not in brk]

p=[]
#자리수보다 1칸더가는경우도 비교
for i in range(1,len(N)+2):
    p+=list(product(remote,repeat=i))

answer=[]
#순수 +,- 로만이동
no=abs(100-int(N))

#버튼과 +,- 로 이동
x,y=999999999,0
for i in range(len(p)):
    s=int("".join(p[i]))
    if x>abs(s-int(N)):
        x,y=abs(s-int(N)),len(p[i])

if no<=x+y:
    print(no)
else:
    print(x+y)
'''

import sys

input=sys.stdin.readline

N=int(input())
M=int(input())
if M:
    brk=list(input().strip())
else:
    brk=[]

answer=abs(N-100)

for cur in range(1000001):
    x=list(str(cur))
    flag=True
    for ele in x:
        if ele in brk:
            flag=False
    if flag:
        answer=min(answer,len(str(cur))+abs(N-cur))
print(answer)






    



