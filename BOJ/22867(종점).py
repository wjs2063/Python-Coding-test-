import re
import datetime as dt
import heapq
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
time=deque()
# heap 에는 in out 순으로
heap=[]
#queue 에는 out 
queue=[]
for _ in range(n):
    heapq.heappush(heap,input().split())
get_in,get_out=heapq.heappop(heap)
heapq.heappush(queue,get_out)

while heap:
    get_in,get_out=heapq.heappop(heap)
    # queue[0]에는 제일 빠른도착
    if queue[0]<=get_in:
        heapq.heappop(queue)
    heapq.heappush(queue,get_out)
print(len(queue))

