from collections import deque
def solution(n, k, cmd):
    answer = ''
    queue=deque()
    select=k
    frame=[i for i in range(n)]
    answer=['O' for _ in range(n)]
    while cmd:
        cmds=cmd.pop(0)
        cmds=cmds.split()
        # U or D 일떄
        if len(cmds)==2:
            if cmds[0]=="D":
                select+=int(cmds[1])
                continue
            if cmds[0]=="U":
                select-=int(cmds[1])
                continue
        #삭제
        if cmds[0]=="C":
            queue.appendleft((select,frame[select]))
            answer[frame[select]]="X"
            del frame[select]
            if select==len(frame):
                select-=1
            continue
        # 복구
        if cmds[0]=="Z":
            memory,origin=queue.popleft()
            answer[origin]='O'
            frame.insert(memory,origin)
            if select>=memory:
                select+=1
                continue
            
            
    answer="".join(answer)
    
    return answer