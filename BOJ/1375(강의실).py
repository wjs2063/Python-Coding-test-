import heapq
import sys
input=sys.stdin.readline
n=int(input())

heap=[]
queue=[]
count=0
# heap 에는 [start,end,num] 즉 start기준으로정렬됨
# start 가 가장 작은것이 먼저 빠져나온다
for _ in range(n):
    num,start,end=map(int,input().split())
    heapq.heappush(heap,[start,end,num])
start,end,num=heapq.heappop(heap)
heapq.heappush(queue,end)

while heap:
    start,end,num=heapq.heappop(heap)
    # 종료시간 ->q[0] 강의실 시작시간보다 작거나같다면
    if queue[0]<=start:
        heapq.heappop(queue)
        # heapq 에서 꺼내자
    heapq.heappush(queue,end)
print(len(queue))
