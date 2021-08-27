import sys
from itertools import permutations
input=sys.stdin.readline
number=[]
n=int(input())
k=int(input())

for _ in range(n):
    number.append(int(input()))
#방문한 곳 체크
visited=[False]*n
#담을 변수
result=[]
s=[]
def my_card(x):
    global s
    if x>=k:
        result.append("".join(s))
        return
    for i in range(n):
        # 방문했으면 건너뛰고
        if visited[i]:
            continue
        visited[i]=True
        s.append(str(number[i]))
        my_card(x+1)
        s.pop()
        visited[i]=False
    return
my_card(0)
print(len(set(result)))

        
        


