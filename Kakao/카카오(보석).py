gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# 투포인터 방식을 쓰지않으면 O(n^2) 으로 효율성테스트 통과안됨....
from collections import deque,defaultdict
def solution(gems):
    answer = []
    result=[]
    kind=set(gems) #종류
    start,end=0,0
    cart=defaultdict(int)
    cart[gems[0]]+=1
    while start<len(gems) and end<len(gems):
        if len(cart)<len(kind):
            end+=1
            if end==len(gems):
                break
            cart[gems[end]]+=1
        else:
            result.append((end-start,start+1,end+1))
            cart[gems[start]]-=1
            if cart[gems[start]]==0:
                del cart[gems[start]]
            start+=1
    result.sort(key=lambda x:(x[0],x[1]))
    answer.append(result[0][1])
    answer.append(result[0][2])
    
    
                
            
    
    return answer