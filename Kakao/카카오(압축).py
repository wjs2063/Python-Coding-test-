from collections import deque
msg="TOBEORNOTTOBEORTOBEORNOT"
alphabet={}
x=ord('A')
for i in range(1,27):
    alphabet[chr(x+i-1)]=i
def search(msg:deque):
    if len(msg)<=0:
        return False
    
a="123"
print(alphabet.keys())

def solution(msg:str):
    answer=[]
    this=0
    end=False
    dict_index=26
    while True:
        if msg=="":
            break
        i=0
        while i<len(msg):
            if msg[:i+1] in alphabet.keys():
                i+=1
            else:
                break
        # i 의 값이 반영되어나옴 즉 0<= x<=i-1 까지 포함되어있다는말
        
        #dict index 1증가후
        if msg[:i+1] not in alphabet.keys(): 
            dict_index+=1
            # 사전저장
            alphabet[msg[:i+1]]=dict_index
        # 그리고 i-1 까지 단어 출력배열에 추가
        answer.append(alphabet[msg[:i]])
        msg=msg[i:]
    return answer

print(solution(msg))



        

