from itertools import permutations

exp="100-200*300-500+20"

opt="*+-"
answer=0
priorities=list(permutations(opt))

max_val=0
answer=0
for prior in priorities:
    # 우선순위가 제일 적은 애로 먼저 split
    result=[]
    
    one = exp.split(prior[2])
    
    # 그다음 우선순위로  split
    for element in one:
        s=element.split(prior[1])
        se2=[str(eval(e1)) for e1 in s]
        # 최고우선순위먼저계산해주기
        result.append(prior[1].join(se2))
    result=[str(eval(e1)) for e1 in result]
    max_val=abs(eval(prior[2].join(result)))
    
    if max_val>answer:
        answer=max_val
    # 큰값을 answer 에 넣어주기 
print(answer)