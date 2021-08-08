n=int(input())
atm_time=list(map(int,input().split()))
atm_time.sort()
time=0

for i in range(len(atm_time)):
    time+=sum(atm_time[:i+1])
print(time)
