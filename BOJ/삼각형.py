from collections import deque
test_case=deque()
while True:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    test_case.append(a)
# test case 담기
while test_case:
    test=test_case.popleft()
    n=test.pop(0)
    



    
