m="ABCDEFG"
musicinfos=["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
note=['C#','D#','F#','G#','A#','C','D','E','F','G','A','B']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l']
import re
def solution(t,musicinfos):
    result=[]
    for idx,musicinfo in enumerate(musicinfos):
        m=musicinfo.split(",")
        s_h,s_m=map(int,m[0].split(":"))
        e_h,e_m=map(int,m[1].split(":"))
        play_time=60*(e_h-s_h)+(e_m-s_m)
        name=m[2]
        sheet_music=m[3]
        for idx,n in enumerate(note):
            t=re.sub(n,alpha[idx],t)
            sheet_music=re.sub(n,alpha[idx],sheet_music)
        repeat,mod=divmod(play_time,len(sheet_music))
        total_rhythm=sheet_music*repeat+sheet_music[:mod]

        for i in range(len(total_rhythm)-len(t)+1):

            if total_rhythm[i:i+len(t)]==t:
                r=(play_time,idx,name)
                result.append(r)
                break
    if len(result)==0:

        return '(None)'
    result.sort(key=lambda x:(-x[0],x[1]))
    return result[0][2]

print(solution(m,musicinfos))


        

