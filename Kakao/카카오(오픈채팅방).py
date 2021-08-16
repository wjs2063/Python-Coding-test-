record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

from collections import defaultdict
import re
def solution(record):
    answer = []
    change_dict=defaultdict(list)
    record=list(map(lambda x:tuple(x.split()),record))
    #변경한 new_id 가있다면 change dict 에 넣어주고 기록
    #변경하지않았으면 origin 에 넣어줌
    for i in range(len(record)):
        if record[i][0] in ('Change','Enter'):
            change_dict[record[i][1]].append(record[i][2])
    # 해당 id 가변경한 기록이있다면 최근기록을반영해서 바꾸어줌 change 인경우pass
    for i in range(len(record)):
        if record[i][1] in change_dict.keys():
            if record[i][0]=='Enter':
                s=change_dict[record[i][1]][-1]
                answer.append(s+"님이 들어왔습니다.")
                continue
            elif record[i][0]=='Leave':
                s=change_dict[record[i][1]][-1]
                answer.append(s+"님이 나갔습니다.")
                continue
            else :
                continue
    
    return answer
print(solution(record))