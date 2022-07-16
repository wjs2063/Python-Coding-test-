import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
k=list(map(int,input().split()))
q=deque([i for i in range(1,n+1)])
n=n-1
def left():
    f=q[0]
    q.popleft()
    q.append(f)
def right():
    f=q[-1]
    q.pop()
    q.appendleft(f)

answer=0
for x in k:
    index=q.index(x)
    #print("실행전 : ",q)
    if index<=n-index+1:
        for _ in range(index):
            left()
        answer+=index
        q.popleft()
    else:
        for _ in range(n-index+1):
            right()
        answer+=n-index+1
        q.popleft()
    n-=1
    #print("실행후 : ",answer,q,n) T: O(K*N^2)
print(answer)
