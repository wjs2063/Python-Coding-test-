n=int(input())
from itertools import combinations
word_list=[]
alphabet="0123456789"
for i in range(1,10+1):
    words=list(combinations(alphabet,i))
    for k in range(len(words)):
        a=list("".join(words[k]))
        a.sort(reverse=True)
        t=int("".join(a))
        word_list.append(t)
word_list.sort()
if n>=len(word_list):
    print(-1)
else:
    print(word_list[n])

