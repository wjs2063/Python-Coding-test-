def is_right_str(t):
    
    stack=[]
    stack.append(t[0])
    for i in range(1,len(t)):
        stack.append(t[i])
        if len(stack)>1:
            if stack[-1]==")" and stack[-2]=="(":
                stack.pop()
                stack.pop()
    
    if stack:
        return False
    return True
## 한번 실패하면 오류 잡기 너무 힘들다...
def solution(p):
    answer = ''
    #1단계
    u=""
    v=""
    if p=="" or is_right_str(p):
        return p
    #2단계
    for i in range(1,len(p),2):
        u=p[:i+1]
        v=p[i+1:]
        
        if u.count("(")==u.count(")") and v.count("(")==v.count(")"):
            
            break
    if is_right_str(u):
        return u+solution(v)
    answer+="("+solution(v)+')'
    u=u[1:-1]
    
    for i in range(len(u)):
        if u[i]=="(":
            answer+=")"
        else:
            answer+="("
    
    return answer
p="()))((()"
print(solution(p))