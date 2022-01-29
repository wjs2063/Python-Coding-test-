import sys
import heapq
from itertools import combinations
n,m=map(int,sys.stdin.readline().rstrip().split())
city=[]

 
for _ in range(n):
    city.append(list(map(int,sys.stdin.readline().rstrip().split())))
chicken=[]
home=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            chicken.append((i,j))
        if city[i][j]==1:
            home.append((i,j))
chicken_pos=combinations(chicken, m)

f=[]
for chicken_poss in chicken_pos:
    answer=0
    for hh in home:
        distance=[]
        for chic in chicken_poss:
            d=abs(chic[0]-hh[0])+abs(chic[1]-hh[1])
            heapq.heappush(distance,d)
        answer+=heapq.heappop(distance)
    f.append(answer)
print(min(f))

        



