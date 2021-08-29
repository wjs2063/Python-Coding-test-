
play_time="02:03:55"
adv_time="00:14:15"
logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
def time_to_int(strs):
    h,m,s=map(int,strs.split(':'))
    return h*3600+m*60+s

def int_to_time(s):
    time=''
    #시간
    h=s//3600
    s=s-h*3600
    #분
    m=s//60
    s=s-m*60
    #초
    h=str(h).zfill(2)
    m=str(m).zfill(2)
    s=str(s).zfill(2)
    return h+":"+m+":"+s

def solution(play_time,adv_time,logs):
    play_time=time_to_int(play_time)
    adv_time=time_to_int(adv_time)
    watch_person=[0 for _ in range(play_time+1)]
    for log in logs:
        start,end=map(time_to_int,log.split('-'))
        watch_person[start]+=1
        watch_person[end]-=1
    #여기까지 완료하면 광고의 시작-끝 
    for i in range(1,play_time+1):
        watch_person[i]+=watch_person[i-1]
    # 여기까지완료하면 광고 재생 각 시점마다 사람의 수
    for i in range(1,play_time+1):
        watch_person[i]+=watch_person[i-1]
    # 누적 sum
    most_view=watch_person[adv_time-1]
    most_view_start=0
    for e in range(adv_time,play_time):
        if most_view<watch_person[e]-watch_person[e-adv_time]:
            most_view=watch_person[e]-watch_person[e-adv_time]
            most_view_start=e-adv_time+1
    return int_to_time(most_view_start)

print(solution(play_time,adv_time,logs))

    
    
    
    
    






    


    
