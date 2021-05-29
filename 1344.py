
from math import sqrt,floor
probability_a=float(input())/100
probability_b=float(input())/100

# prob[x][a][b]--> x번째 간격까지 score A=a,B=b일 확률
a1=(1-probability_a)*(1-probability_b)
a2=(1-probability_a)*probability_b
a3=probability_a*(1-probability_b)
a4=probability_a*probability_b

prob=[[[0 for i in range(19)]for i in range(19)]for i in range(19)]


prob[1][0][0]=a1
prob[1][0][1]=a2
prob[1][1][0]=a3
prob[1][1][1]=a4

for i in range(2,18+1):
    for j in range(18+1):
        if j>i:
            break
        for k in range(18+1):
            if k>i:
                break
            prob[i][j][k]+=prob[i-1][j][k]*a1
            if j>0:
                prob[i][j][k]+=prob[i-1][j-1][k]*probability_a*(1-probability_b)

            if k>0:
                prob[i][j][k]+=prob[i-1][j][k-1]*probability_b*(1-probability_a)
            if j>0 and k>0:
                prob[i][j][k]+=prob[i-1][j-1][k-1]*probability_a*probability_b
def isprime(number):
    if number==0 or number==1:
        return False
    for i in range(2,floor(sqrt(number))+1):
        if number%i==0:
            return False
        
    return True

final_answer=0

for i in range(18+1):
    for j in range(18+1):
        if isprime(i) or isprime(j):
            final_answer+=prob[18][i][j]
        
print(final_answer)


