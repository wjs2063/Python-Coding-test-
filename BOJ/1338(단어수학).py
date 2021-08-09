from collections import deque,defaultdict
n=int(input())
words=[]
for _ in range(n):
    words.append(input())
opt=defaultdict(int)


for word in words:
    l=len(word)-1
    for s in word:
        opt[s]+=10**l
        l-=1
answer=[]


for value in opt.values():
    answer.append(value)
answer.sort(reverse=True)
#내림차순 정렬 
number=[9,8,7,6,5,4,3,2,1,0]
result=0
for i in range(len(answer)):
    result+=answer[i]*number.pop(0)
print(result)













