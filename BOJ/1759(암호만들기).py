import sys
from itertools import combinations, combinations_with_replacement
input=sys.stdin.readline
L,C=map(int,input().split())
word_list=input().split()
p=['a','e','i','o','u']
m=[]
t=[]
for x in word_list:
    if x in p:
        m.append(x)
    else:
        t.append(x)
word=[]
for i in range(1,L-1):
    combination_m=list(combinations(m,i))
    combination_t=list(combinations(t,L-i))
    for k in range(len(combination_m)):
        s1=combination_m[k]
        for l in range(len(combination_t)):
            s2=combination_t[l]
            s=list(s1+s2)

            s.sort()
            s="".join(s)
            word.append(s)
word.sort()
for i in word:
    print(i)

