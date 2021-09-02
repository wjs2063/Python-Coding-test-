from collections import deque
v,m=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(v+1)
def bfs(x):
    queue=deque([])
    queue.append(x)
    cnt=0
    while queue:
        v1=queue.popleft()
        if not visited[v1]:
            cnt=1
            visited[v1]=True
            for t in graph[v1]:
                queue.append(t)
    return cnt
cnt=0
for i in range(1,v+1):
    if not visited[i]:
        cnt+=bfs(i)
print(cnt)



