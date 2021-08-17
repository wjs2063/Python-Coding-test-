import re
s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
s=s[2:-2]
s=s.split("},{")
s.sort(key=len)
result=[]
for strs in s:
    t=strs.split(",")
    for t1 in t:
        t1=int(t1)
        if t1 not in result:
            result.append(t1)
print(result)


