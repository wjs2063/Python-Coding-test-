from itertools import combinations
import copy
relation= [['a', 'aa'], ['aa', 'a'], ['a', 'a']]


def isunique(com,relation):
    a=[]
    for combi in com:
        test=list()
        for row in range(len(relation)):
            c=[]
            for col in combi:
                c.append(relation[row][col])
            test.append(tuple(c))
        if len(set(test))==len(relation):
            a.append(combi)
 
    return a




                

# minimal 찾는거는 ..
def minimal(val):
    cnt=0
    while val:
        e=val.pop(0)
        e_len=len(e)
        ex=copy.copy(val)
        for i in range(len(val)):
            # e가 val[i] 번째 집합의 부분집합중 길이가 e_len 인것에 포함되어있다면 삭제
            if e in list(combinations(val[i],e_len)):
                ex.remove(val[i])
        # 변경된 ex 를 다시 val 변수에 넣어주기
        val=ex
        print(val)
        cnt+=1
    return cnt
def solution(relation):


    column=[i for i in range(len(relation[0]))]
    val=[]
    # 유니크한것들만 모아주기
    for i in range(1,len(column)+1):
        # com 에는 i개만큼의 조합경우가 담겨있음
        com=list(combinations(column,i))
        val+=isunique(com,relation)
    print(val)
    # minimal 찾아주기
    val.sort(key=len)
    #길이로 소팅해준후에
    result=minimal(val)
    return result

print(solution(relation))

    

    


