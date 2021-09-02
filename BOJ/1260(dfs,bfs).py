from collections import deque
n,m,t=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# sorting
def dfs(v):
    visited=[False]*(n+1)
    stack=list()
    stack.append(v)
    while stack:
        v=stack.pop()
        if not visited[v]:
            print(v,end=' ')
            visited[v]=True
            for x in sorted(graph[v],reverse=True):
                stack.append(x)



def bfs(v):
    visited=[False]*(n+1)
    queue=deque([])
    queue.append(v)
    while queue:
        v=queue.popleft()
        if not visited[v]:
            print(v,end=' ')
            visited[v]=True
            for x in sorted(graph[v]):
                queue.append(x)
dfs(t)
print()
bfs(t)
