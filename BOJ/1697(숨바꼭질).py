import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())

def bfs(v):
    cnt=0
    dq=deque([[v,cnt]])
    while dq:
        x1,cnt=dq.popleft()
        if not visited[x1]:
            visited[x1]=True
            if x1==k:
                return cnt
            cnt+=1
            if (x1*2)<100001:
                dq.append([2*x1,cnt])
            if (x1+1)<100001:
                dq.append([x1+1,cnt])
            if (x1-1)>=0:
                dq.append([x1-1,cnt])
    return cnt
visited=[False]*100001

print(bfs(n))








