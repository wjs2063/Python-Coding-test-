from collections import defaultdict
def solution(k, dungeons):
    info=defaultdict(list)
    dungeons.sort(key=lambda x:(-x[0]))
    n=len(dungeons)
    answer=0
    def back(dungeons,k,path,t):
        nonlocal answer
        answer=max(answer,t)
        for i in range(n):
            min_tired,use_tired=dungeons[i]
            if i+1 not in path:
                if k>=min_tired:
                    path.add(i+1)
                    k-=use_tired
                    back(dungeons,k,path,t+1)
                    k+=use_tired
                    path-={i+1}
    back(dungeons,k,set(),0)
    # 백트랙킹 구현
    
