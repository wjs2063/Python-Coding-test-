from itertools import combinations
from collections import Counter
orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
def solution(orders,course):
    result=[]
    for c in course:
        test=[]
        for order in orders:
            a=combinations(sorted(order),c)
            test+=a
        most=Counter(test).most_common()

        for key,value in most:
            if value>1 and value==most[0][-1]:
                result.append("".join(key))
    return sorted(result)
    
print(solution(orders,course))