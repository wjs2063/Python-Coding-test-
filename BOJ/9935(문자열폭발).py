import re
from collections import deque
my_str=input().rstrip()
explosion_str=input().rstrip()
# 정규식은 48% 에서 시간초과뜬다...
def solution(my_str,explosion_str):
    # 단어형태로 처리하려면 튜플사용
    p=re.compile(f'({explosion_str})+')
    a=-1
    while a!=len(my_str):
        a=len(my_str)
        my_str=p.sub("",my_str)
        
    a=my_str
    if a=="":
        print("FRULA")
        return
    print(a)
    return
def solution2(my_str,explosion_str):
    last=explosion_str[-1]
    stack=list()
    l=len(explosion_str)
    for strs in my_str:
        # 문자추가
        stack.append(strs)
        if strs==last and "".join(stack[-l:])==explosion_str:
            #삭제
            del stack[-l:]
    answer="".join(stack)
    if answer=="":
        print("FRULA")
    else :
        print(answer)
solution2(my_str,explosion_str)
