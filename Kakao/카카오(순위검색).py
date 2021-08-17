import re
info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    info=list(map(lambda x:x.split(),info))
    query=list(map(lambda x:re.sub("and","",x),query))
    query=list(map(lambda x:x.split(),query))
    for i in range(len(query)):
        cnt=0
        for j in range(len(info)):
            flag=True
            for k in range(5):
                if k==4:
                    if int(info[j][k])>=int(query[i][k]) or query[i][k]=='-':
                        continue
                    else:
                        flag=False
                        break
                if info[j][k]==query[i][k] or query[i][k]=='-':
                    continue
                flag=False
            
            if flag:
                cnt+=1
        answer.append(cnt)     
    return answer
print(solution(info,query))

a=[1,2,3,4,5,6]

a[0],a[1]=a[2],a[3]
print(a)