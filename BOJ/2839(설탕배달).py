weight=int(input())
# 5의 배수이거나 3의배수라면

x=weight//5 # 5로나눈 몫을 저장한다
# 5x+3y=weight, x+y=k 방정식의 해들중  k 의 최솟값을 찾아야한다(그래프관점)
# 5로나눈 몫일때 최댓값을 가지게되는데 그때 y값이 자연수여야 해당  
r=0
for i in range(x,-1,-1):
    print(i)
    y=(weight-5*i)//3
    # y가 정수라면 i+y 를 return 
    if (weight-5*i)%3==0:
        r=-1
        print(i+y)
        break
if r!=-1:
    print(-1)

