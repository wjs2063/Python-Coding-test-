import sys
import bisect
import sys
n=int(sys.stdin.readline().strip())

sequence=list(map(int,sys.stdin.readline().split()))

q=[sequence[0]]
t=[]
for x in sequence:
    if x>q[-1]:
        q.append(x)
        t.append((len(q)-1,x))
        #길이와 원소 저장
    else:
        idx=bisect.bisect_left(q,x)
        q[idx]=x
        t.append((idx,x))
idx=len(q)-1
answer=[]
for i in range(n-1,-1,-1):
    if t[i][0]==idx:
        answer.append(t[i][1])
        idx-=1
print(len(q))
print(*reversed(answer))

