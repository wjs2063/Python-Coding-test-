def solution(infos, actions):
    answer = []
    login=[False for _ in range(len(infos))]
    my_cart=[]
    for action in actions:
        #로그인이 되어있는지 여부는 login 에 담겨있음
        if action[0]=='L':
            # 이미 로그인했으므로 
            if sum(login)!=0:
                answer.append(False)
                continue
            # 문자 parsing
            action=action.split()
            log_id_pass=action[1]+" "+action[2]
            print(log_id_pass)
            # infos 와 확인
            for i in range(len(infos)):
                print(infos[i],log_id_pass)
                if infos[i]==log_id_pass:
                    login[i]=True
                    break
            if sum(login)!=0:
                answer.append(True)
            else:
                answer.append(False)
            # i번째 login 에 True 넣고 break
        # ADD 부분
        if action[0]=='A':
            #로그인 안했다면
            if sum(login)==0:
                answer.append(False)
                continue
            action=action.split()
            my_cart.append("food")
            answer.append(True)
            continue
        if action=="ORDER":
            if len(my_cart)==0:
                answer.append(False)
                continue
            answer.append(True)
            my_cart=[]
            
            
                
            
        
                    
                
        
        
    
    return answer
infos = ["kim password", "lee abc"]
actions = [
    "LOGIN lee abc", 
    "LOGIN kim password"
]
print(solution(infos,actions))