import re
n=int(input())
p=re.compile('(100+1+|01)+')

for _ in range(n):

    contact=input().rstrip()
    a=p.fullmatch(contact)
    
    if a==None:
        print("NO")
    else:
        print("YES")








