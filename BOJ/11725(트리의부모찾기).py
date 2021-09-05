from collections import deque
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
queue=deque([1])
visited=[False ]*(n+1)
parent={}
while queue:
    q=queue.pop()
    for x in graph[q]:
        if not visited[x]:
            visited[x]=True
            parent[x]=q
            queue.append(x)
for i in range(2,n+1):
    print(parent[i])


