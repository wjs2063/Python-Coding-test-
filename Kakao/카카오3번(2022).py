from collections import defaultdict
fees=[180, 5000, 10, 600]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fee[0]:기본시간
# fee[1]:기본요금
# fee[2]:단위시간
# fee[3]:단위요금
import math
def count_fee(time,fees):
    total=fees[1]+math.ceil(max(time-fees[0],0)/fees[2])*fees[3]
    return total

def solution(fees,records):
    car=defaultdict(list)
    a=list()
    for record in records:
        time,number,state=record.split()
        car[number].append(time)

    for c,value in car.items():
        # 길이가 홀수냐 짝수냐
        #그냥 누적시간으로하는구나..reset되는게아님
        if len(value)%2==1:
            time=0
            for i in range(0,len(value)-1,2):
                h1,m1=map(int,value[i].split(':'))
                h2,m2=map(int,value[i+1].split(':'))
                time+=60*(h2-h1)+(m2-m1)
            h,m=map(int,value[-1].split(':'))
            time+=60*(23-h)+(59-m)
            total=count_fee(time,fees)
            a.append([c,total])

        else:
            time=0
            for i in range(0,len(value),2):
                h1,m1=map(int,value[i].split(':'))
                h2,m2=map(int,value[i+1].split(':'))
                time+=60*(h2-h1)+(m2-m1)
            total=count_fee(time,fees)
            a.append([c,total])

    a.sort(key=lambda x:x[0])
    result=[]
    for i in range(len(a)):
        result.append(a[i][1])
    return result
print(solution(fees,records))
    
    





