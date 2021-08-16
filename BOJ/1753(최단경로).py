import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
start=int(input())
INF=int(1e10)
distance=[INF]*(n+1)
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
for i in range(1,n+1):
    if len(graph[i])==0:
        continue
    graph[i].sort(key=lambda x:(x[0],x[1]))
##중복간선이 존재할수있으므로 node,cost 순으로 오름차순 정리를 해주자 
# 안해주면 뒤에 최솟값이 오는경우 반영못함


    

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])


