import re
a="1D2S#10S"
def solution(a):
    bonus={'S':1,'D':2,'T':3}
    optional={"":1,"*":2,"#":-1}
    # 튜플형태로 지정해주면 각 지정 format 에맞는것 반환  없으면 공백
    p=re.compile('([\d]+)([SDT])([*#]?)')
    # 첫번째 숫자가 1개이상, 두번쨰로 S or D or T 중 match 세번째 * # 이 있거나없거나  없으면 공백 형태로반환
    s=p.findall(a)
    
    #기본적인 구조 -> 숫자 +[SDT]+[option] parsing 후
    for i in range(len(s)):
        # 이전항 *2배 해주기 옵션
        if s[i][2]=="*" and i>0:
            s[i-1]=s[i-1]*2
        s[i]=int(s[i][0])**bonus[s[i][1]]*optional[s[i][2]]
    
    answer=sum(s)
    return answer
print(solution(a))
    
    
