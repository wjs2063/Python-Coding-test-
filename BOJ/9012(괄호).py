import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
def vsp(x:deque):
    s=deque()
    for _ in range(len(x)):
        a=x.popleft()
        if len(s)!=0:
            if s[-1]=='(' and a==')':
                s.pop()
                continue
        s.append(a)
    if len(s)!=0:
        return False
    return True
            




for _ in range(T):
    strs=input().rstrip()
    strs=deque(strs)
    if vsp(strs):
        print("YES")
    else:print('NO')

