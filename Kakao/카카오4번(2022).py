from itertools import combinations

n=10
info=[0,0,0,0,0,0,0,0,3,4,3]

def solution(n,info):
    a=[i for i in range(11)]
    score=[]
    # 라이언이 이길 횟수를 구해야함
    for num in range(n+1):
        t=list(combinations(a,num))
        for x in t:
            cnt=n
            ryan=[ 0 for _ in range(11)]
            ryan_state=[0 for _ in range(11)]
            state=[False]*11
            for win in x:
                # 점수 갱신
                # win index 는 ryan 이이기는 곳
                ryan[win]=(10-win)
                # 횟수 차감
                cnt-=info[win]+1
                ryan_state[win]=info[win]+1
                state[win]=True
            if cnt<0:
                continue
            i=0
            while cnt>0:
                for i in range(10,-1,-1):
                    if not state[i]:
                        ryan_state[i]=min(cnt,info[i])
                        cnt-=min(cnt,info[i])
            r=sum(ryan)
            s=0
            for i in range(11):
                if not state[i] and info[i]>0:
                    s+=10-i
            if r>s:
                ryan_state.append(r-s)
                score.append(ryan_state)
    if len(score)==0:
        return [-1]
    score.sort(key=lambda x:(x[-1],x[-2],x[-3],x[-4],x[-5],x[-6],x[-7],x[-8],x[-9],x[-10],x[-11],x[-12]))
    result=score[-1][:-1]
    
    return result
print(solution(n,info))