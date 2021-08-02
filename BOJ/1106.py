from typing import MutableMapping


c,n=map(int,input().split())
information=[]
for i in range(n):
    information.append(list(map(int,input().split())))
    

min_cost=[0 for i in range(2000+1)]

for cost,people in information:
    for cur_people in range(people,c+101):
        min_cost[cur_people]=min(min_cost[cur_people],min_cost[cur_people-people]+cost)

print(min(min_cost[c:c+101]))






        
        
        
            








