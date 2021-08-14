n=5
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]

def solution(n,arr1,arr2):
    result=[]
    answer=[]
    for i in range(n):
        real=bin(arr1[i]|arr2[i])[2:]
        
        real=real.zfill(n)
        result.append(real)
    
    for strs in result:
        val=""
        for alphabet in strs:
            if alphabet=="1":
                val+="#"
            else:
                val+=" "
        answer.append(val)
    return answer
print(solution(n,arr1,arr2))
 
