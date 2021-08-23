import re
import bisect
infos=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

query=list(map(lambda x:re.sub("and","",x).split(),query))
print(query)
result=[]
language=['cpp','python','java']
job=['backend','frontend']
career=['senior','junior']
food=['pizza','chicken']
information={}
def calc(frame,a,b,c,d,e):
    if a=='-':
        cnt=0
        for item in language:
            cnt+=calc(frame,item,b,c,d,e)
        return cnt
    if b=='-':
        cnt=0
        for item in job:
            cnt+=calc(frame,a,item,c,d,e)
        return cnt
    if c=='-':
        cnt=0
        for item in career:
            cnt+=calc(frame,a,b,item,d,e)
        return cnt
    if d=='-':
        cnt=0
        for item in food:
            cnt+=calc(frame,a,b,c,item,e)
        return cnt
        
    idx=bisect.bisect_left(frame[a][b][c][d],e)
    return len(frame[a][b][c][d])-idx
def solution(infos,query):
    for l in language:
        information[l]=dict()
        for j in job:
            information[l][j]=dict()
            for c in career:
                information[l][j][c]=dict()
                for f in food:
                    information[l][j][c][f]=list()
    # language, job, career,food, score 순
    for person in infos:
        p1,p2,p3,p4,p5=person.split()
        information[p1][p2][p3][p4].append(int(p5))
    for l in language:
        for j in job:
            for c in career:
                for f in food:
                    information[l][j][c][f].sort()
    for ask in query:
        p1,p2,p3,p4,p5=ask
        result.append(calc(information,p1,p2,p3,p4,int(p5)))
    return result

print(solution(infos,query))
    




