import sys
import re
from collections import deque
T=int(input())
p=[]
arr=deque()
for _ in range(T):
    p.append(input())
    n=int(input())
    strs=input()
    arr.append(strs)
def convert(p,array):
    state=0
    # 0이면 왼쪽에서 1이면 오른쪽에서
    for strs in p:
        try:
            if strs=='R':
                state=(state+1)%2
                continue
            if state==0:
                array.popleft()
            else:
                array.pop()

        except:
            print('error')
            return None
    return array,state
for cmds,array in zip(p,arr):
    if len(array)==2:
        array=[]
    else:
        array=deque(array[1:-1].split(","))

    flag=convert(cmds,array)

    if flag==None:
        continue
    else:
        if flag[1]==0:
            print("["+",".join(list(flag[0]))+"]")
        else :
            print("["+",".join(list(flag[0])[::-1])+"]")
# 출력형식 맞춰야앟ㅁ... 배열 그대로출력하면 [1, 2, 3] -> str 로 [1,2,3]으로바꾸기
        