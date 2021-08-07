from collections import deque

n=int(input())

number=list(map(int,input().split()))
target=int(input())
# 정렬하기
number.sort()

def solution(deque=number,target=target):
    # deque 안에 target 이있다면 제외
    if target in deque:
        return 0
    # target이 queue 의 min 보다작다면 
    if target<deque[0]:
        l=target
        r=deque[0]-target
        answer=l*r-1
        return answer
    
    #target이 queue 의 사이에있다면
    # target 이 포함된 양끝을 알아낸후
     
    for i in range(len(deque)):
        if deque[i]>target:
            last=i
            break
    left=last-1
    right=last
    

    l=target-deque[left]
    r=deque[right]-target
    
    # l*r 만큼의 개수에서 마지막에 [target,target] 인 경우 제외해주면 되므로 -1
    answer=l*r-1
    
    return answer
print(solution(number,target))