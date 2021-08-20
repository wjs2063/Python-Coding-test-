n=int(input())
sequence=[]
sequence_interval=[]
for _ in range(n):
    left,right=map(int,input().split())
    left-=right
    right+=left
    sequence.append((left,right))
    sequence_interval.append((left,right))
## 수열 및 구간 계산
sequence_interval.sort(key=lambda x:(x[1],x[0]))
for x,y in sequence:
    start=0
    end=len(sequence_interval)-1
    while start<=end:
        

