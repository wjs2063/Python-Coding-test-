import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e10)
graph=[[] for _ in range(n+1)]
cost=[ INF for _ in range(n+1)]



for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
start,end=map(int,input().split())
def dijkstra(v):
    q=[]
    # heap 생성
    heapq.heappush(q,(0,v))
    #자기자신으로 가는비용
    cost[v]=0
    while q:
        dist,n=heapq.heappop(q)
        # 현재 n으로 가는 비용이 dist 보다 작다면 무시
        if cost[n]<dist:
            continue
        for i in graph[n]:
            # n과 연결되어있는 지점을 다 꺼내서 check
            pay=i[1]+dist
            # 만약 pay 가 cost 다음지점으로가는 비용보다 작다면
            if pay<cost[i[0]]:
                cost[i[0]]=pay
                heapq.heappush(q,(pay,i[0]))

dijkstra(start)

print(cost[end])




