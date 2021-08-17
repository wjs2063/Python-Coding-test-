import re
str1="E=M*C^2"
str2="e=m*c^2"

def solution(str1,str2):
    if len(str1)==0 and len(str2)==0:
        return 0
    str1=str1.lower()
    str2=str2.lower()
    s1=[]
    s2=[]
    for i in range(len(str1)-1):
        s=re.sub(r"[^a-z]","",str1[i:i+2])
        if len(s)!=2:
            continue
        s1.append(s)
    for i in range(len(str2)-1):
        s=re.sub(r"[^a-z]","",str2[i:i+2])
        if len(s)!=2:
            continue
        s2.append(s)
    s1_set=set(s1)
    s2_set=set(s2)
    union_set=s1_set | s2_set
    intersect=0
    union=0
    for s in union_set:
        min_val=min(s1.count(s),s2.count(s))
        max_val=max(s1.count(s),s2.count(s))
        intersect+=min_val
        union+=max_val
    if union==0:
        return int(65536)
    answer=int(intersect/union * 65536)
    return answer
print(solution(str1,str2))
