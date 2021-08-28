from collections import defaultdict
n=int(input())
c=int(input())
visited=[False]*(n+1)
graph=defaultdict(list)
for _ in range(c):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
def dfs(x):
    global cnt
    if not visited[x]:
        visited[x]=True
        cnt+=1

        # graph[x]에있는 모든 컴퓨터에대해 dfs 수행
        for computer in graph[x]:
            dfs(computer)
            
dfs(1)
# 1번컴퓨터는뺴야함
print(cnt-1)




