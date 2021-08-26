number={0:"0",
1:"1",
2:"2",
3:"3",
4:"4",
5:"5",
6:"6",
7:"7",
8:"8",
9:"9",
10:"A",
11:"B",
12:"C",
13:"D",
14:"E",
15:"F"}

def solution(n,t,m,p):
    i=1
    s="0"
    a=1
    while i<=m*t:
        n_th=a
        strs=""
        while n_th!=0:
            n_th,r=divmod(n_th,n)
            strs+=number[r]
            i+=1
        s+=strs[::-1]
        a+=1
    answer=""
    for idx in range(p,m*t+1,m):
        answer+=s[idx-1]
    
    return answer
print(solution(16,16,2,2))




