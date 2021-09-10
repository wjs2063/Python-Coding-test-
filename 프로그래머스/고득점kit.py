from itertools import permutations,combinations
numbers=[1,1,1,1,1]
target=3
def solution(numbers, target):
    answer = 0
    n=len(numbers)
    cnt=0
    result=[0]
    for num in numbers:
        opt=[]
        for x in result:
            opt.append(x+num)
            opt.append(x-num)
        result=opt
    for r in result:
        if r==target:
            cnt+=1
    return cnt
print(solution(numbers,target))
    