import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline
strs=input().rstrip()
stack=list()
word=list()
index_list=list()
for i in range(len(strs)):
    if strs[i]=='(':
        stack.append((i,strs[i]))
        continue
    if strs[i]==')':
        x,y=stack.pop()
        index_list.append((x,i))
# index_list 에 괄호 위치정보 저장
for i in range(1,len(index_list)+1):
    a=list(combinations(index_list,i))
    
    for x in a:
        result=list(strs)
        b=list()
        r=""
        for y in x:
            m,n=y
            b.append(m)
            b.append(n)
        for i in range(len(result)):
            if i in b :
                continue
            r+=result[i]
        word.append(r)
word=set(word)
word=list(word)
word.sort()
for x in word:
    print(x)
    

            

        


    

    
    