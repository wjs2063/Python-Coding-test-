import re
files=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

#print(re.findall(r'\D+',files))
#print(re.findall(r'[0-9]{1,5}',files))

def solution(files):
    word=[]
    relate=[]
    # 첫번째
    for idx,file in enumerate(files):
        # head,number
        info=(re.findall(r'[\D]+',file)[0],re.findall(r'[0-9]+',file)[0])
        x=len(info[0])
        x+=len(info[1])
        #tail
        tail=file[x:]
        relate.append((info[0].lower(),int(info[1]),idx))
    relate.sort(key=lambda x:(x[0],x[1],x[2]))
    for i in range(len(relate)):
        word.append(files[relate[i][2]])
    return word
print(solution(files))

        