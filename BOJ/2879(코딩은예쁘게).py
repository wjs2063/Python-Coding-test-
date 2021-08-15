n=int(input())
now=list(map(int,input().split()))
target=list(map(int,input().split()))
# need 를 0을 만드는게 목표임
need=list()
for i in range(n):
    need.append(now[i]-target[i])
def solution():
    left,right=0,1
    cnt=0
    while left<n:
        
        # insert 하는 과정
        if need[left]>=0:
            left+=1
            right+=1
            continue
        if right<n:
            if need[right]<0:
                right+=1
                continue
        min_val=max(need[left:right])
        for i in range(left,right):
            need[i]-=min_val # min_val 은 음수라서 그냥 뺴주면된다
        cnt-=min_val
        right=left+1
        ## left:right 의 max 찾고 뺴줌(음수라서)
    left,right=0,1
    while left<n:
        
        if need[left]<=0:
            left+=1
            right+=1
            continue
        if right<n:
            if need[right]>0:
                right+=1
                continue
        min_val=min(need[left:right])
        for i in range(left,right):
            need[i]-=min_val
        cnt+=min_val
        right=left+1
    return cnt
print(solution())
        
        


