import sys
from collections import deque
input=sys.stdin.readline
S=input().rstrip()
T=input().rstrip()

def solution(S,T):
    while len(T)>=len(S):
        if T==S:
            return 1
        if T[-1]=='A':
            T=T[:-1]
            continue
        if T[-1]=='B':
            T=T[:-1]
            T=T[::-1]
            continue
    return 0
print(solution(S,T))


    

