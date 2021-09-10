from collections import defaultdict
k=10
room_number=[1,3,4,1,3,1]
# 정확성 1,2만통과한 솔루션 ㅠㅠ
def solution(k,room_number):
    your_room=dict()
    result=[]
    # 과거 x번을 원했던 사람이 들어간 방 번호
    past=dict()
    for x in room_number:
        try:
            # room_number 에 값이 있다면
            a=x 
            while your_room[x]:
                x=your_room[x]+1
        except:
            # room_number 에 값이없다면
            your_room[a]=x
            past[a]=x
            your_room[x]=x
            # a번을 원했던사람은 x번에 들어가게됨
            past[a]=x
            result.append(x) 
    return result
print(solution(k,room_number))

## 시간초과해결
def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        # 방문한 기록 추가
        visit = [n]
        # 방번호 n 이 room_dic에 없어질떄 빠져나오기
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
    return ret