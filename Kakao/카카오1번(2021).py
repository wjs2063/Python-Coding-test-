id_list=["con", "ryan"]
report=["ryan con", "ryan con", "ryan con", "ryan con"]
k=2
from collections import defaultdict
def solution(id_list,report,k):
    candidate=dict()
    banned=defaultdict(int)
    my=defaultdict(list)
    repeat=set()
    result=[]
    for name in report:
        user,ban_id=name.split()
        if name not in repeat:
            repeat.add(name)
            banned[ban_id]+=1
            my[user].append(ban_id)
    for name in id_list:
        
        cnt=0
        # my[user]에 담긴 id 들중 ban 당한횟수
        for id in my[name]:
            if banned[id]>=k:
                cnt+=1
        result.append(cnt)
    return result
print(solution(id_list,report,k))

        

    

        