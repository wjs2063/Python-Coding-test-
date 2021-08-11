from collections import deque
N,W,L=map(int,input().split())
truck=deque(map(int,input().split()))
bridge=deque([0 for _ in range(W)],maxlen=W)
#0의 개수 = 빈공간
def solution():
    time=0
    while truck:
        bridge.popleft()
        t=truck[0] # truck 의 첫번째 주자
        if sum(bridge)+t<=L:
            bridge.append(truck.popleft())
        #0을 추가해주는 이유는 시간이지나면서 bridge에있는 truck 이 사라짐
        else :
            bridge.append(0)
        
        time+=1
    return time+W
print(solution())

