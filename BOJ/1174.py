from itertools import combinations

n=int(input().strip())

def check(numbers):
    for j in range(len(numbers)-1):
        if numbers[j]<=numbers[j+1]:
            return False
    return True
    


number=[str(i) for i in range(0,10)]
answer=[]
c=1
while len(answer)<=10**6:
    first_ord=list(combinations(number, c))
    for i in range(len(first_ord)):
        if check(first_ord[i]):
            answer+=list(first_ord[i])
    c+=1
    if c==2:
        break
    
print(answer)

