import sys

input=sys.stdin.readline
result=[]
ex=[]
visited=[False]*10
def back(x,case):
    if x>=len(case):
        ex.append("".join(result))
        return
    for i in range(len(case)):
        if visited[i]:
            continue
        visited[i]=True
        result.append(case[i])
        back(x+1,case)
        result.pop()
        visited[i]=False


while True:
    input_in=input().strip()
    if input_in:
        ex=[]
        result=[]
        case,index=map(str,input_in.split())
        case=list(case)
        back(0,case)
        if int(index)>len(ex):
            print(f'{"".join(case)} {index} = No permutation')
        else:
            print(f'{"".join(case)} {index} = {ex[int(index)-1]}')
        continue
    break
    

