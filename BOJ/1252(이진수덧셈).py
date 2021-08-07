num1,num2=map(str,input().split())
from collections import deque


def half_adder(num1:str,num2:str)->str:
    l1=len(num1)
    l2=len(num2)
    #만약 합이 0이라면 그냥 0 을 return 
    if int(num1)+int(num2)==0:
        return 0
    num1=deque(num1)
    num2=deque(num2)
    #길이맞춰주기
    if l1<l2:
        while(len(num1)<len(num2)):
            num1.appendleft("0")
    elif l2<l1:
        while(len(num2)<len(num1)):
            num2.appendleft("0")
    # (carry+num1[-i]+num2[-i])//2
    carry=0
    answer=""
    for i in range(1,len(num1)+1):
        total=carry+int(num1[-i])+int(num2[-i])
        carry,output=divmod(total,2)
        #str로 바꾼고 추가 
        answer+=str(output)
        if i==len(num1) and carry!=0:
            answer+=str(carry)
    #왼쪽에 0이있다면 제거해주자

    answer=answer[::-1]

    point=0
    for i in range(len(answer)):
        if answer[i]=="1":
            point=i
            break
    answer=answer[point:]
    return answer
print(half_adder(num1,num2))