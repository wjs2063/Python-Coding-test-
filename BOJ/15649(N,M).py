def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(fact(5))
r=2
result=[]
per_array=[1,2,3,4]
used=[False]*len(per_array)

N,M=map(int,input().split())
used=[False]*N
per_array=[i for i in range(1,N+1)]
def permutation(x,M):
    if x>=M:
        print(*result)
        return 
    for i in range(len(per_array)):
        if used[i]==True:
            continue
        used[i]=True
        result.append(per_array[i])
        permutation(x+1,M)
        result.pop()
        used[i]=False
permutation(0,M)

def combination(x):
    if x>=r:
        print(*result)
        return
    for i in range(len(per_array)):
        if used[i]==True:
            continue
        used[i]=True
        result.append(per_array[i])
        combination(x+1)
        result.pop()
        # 다시 False 로 만들어주는 과정
        for j in range(i+1,len(per_array)):
            used[j]=False
print("---combi---")
combination(0)