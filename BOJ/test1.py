from collections import deque


n,m=map(int,input().split())

n_list=list(map(int,input().split()))
answer=[]
for i in range(n):
    answer.append(i+1)


print(n,n_list)
deq=deque(n_list)


def find(answer,x):
    for i in range(len(answer)):
        if answer[i]==x:
            return i
    
length=n
count=0
while length>0:
    index=find(answer,n_list[0])
    if index%length <=(-index)%length:
        deq.rotate(index)
        deq.popleft()
        count+=index%length
        print(count)
    else :
        deq.rotate(-index)
        deq.popleft()
        count+=(-index)%length
        print(count)
    length-=1
    del(n_list[0])
print(count)

