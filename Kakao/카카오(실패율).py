n=4
stages=[4,4,4,4,4]
def solution(N, stages):
    answer = []
    total=len(stages)
    fail=[]
    for i in range(1,N+1):
        if total==0:
            fail.append((i,0))
            continue
        n=stages.count(i)
        fail.append((i,n/total))
        total-=n
        

    fail.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    print(fail)
    for i in range(len(fail)):
        answer.append(fail[i][0])
        
    return answer
print(solution(n,stages))