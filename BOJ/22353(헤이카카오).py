from collections import defaultdict
a,d,k=map(int,input().split())
prob=d
# 한판에 a분 , 승률 d% , 비율 k%
# x판하려면 x-1 번째판까지 지고 x번째판에서 이겨야함
# n판후 이길확률:= An 이라고두자
# An=An-1 * (1+k)
e_x=0
d/=100
k/=100
# x판후 이길확률을 prob_list에 담자
prob_list=[0,d]
# d가 100을 넘는다?
while d<1:
    # prob_list 의 n번쨰인덱스에는 n판만에 처음으로 이길확률
    d=prob_list[-1]*(1+k)
    prob_list.append(d)
# 1이 넘는값은 제거
prob_list.pop()


# idx-1번까지 연속으로 질확률을 반환하는 함수
def loss_prob(idx:int,prob_list:list)->float:
    p=1
    for i in range(1,idx):
        p*=(1-prob_list[i])
    return p
ex=0
prob_sum=0
gap=a
for i in range(1,len(prob_list)):

    prob_sum+=loss_prob(i,prob_list)*prob_list[i]
    
    ex+=a*loss_prob(i,prob_list)*prob_list[i]
    a+=gap
ex+=(a)*(1-prob_sum)

if prob==100:
    print(a)
else:
    print(ex)

    
    


