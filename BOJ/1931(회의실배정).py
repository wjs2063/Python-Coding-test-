n=int(input())
schedule=[]

for _ in range(n):
    s=list(map(int,input().split()))
    schedule.append(s)
# 끝나는 시간을 기준으로 정렬하여야함 끝나는시간이같다면 start 가 빠른순으로 먼저 해주어야함
# (1,2)(2,2) 에서 정렬을 해주면 2개 처리 해주지않는다면 1개로 처리될가능성있음
schedule.sort(key=lambda x:(x[1],x[0]))

prev_end=0
cnt=0
for start,end in schedule:
    if start>=prev_end:
        cnt+=1
        prev_end=end
print(cnt)