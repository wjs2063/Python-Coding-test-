import sys
input=sys.stdin.readline
S=input().rstrip()
P=input().rstrip()
#길이가 100만이라 투포인터?
def solution(S,P):
    i=0
    if S==P:
        return 1
    while i<len(S):
        if S[i]!=P[0]:
            i+=1
            continue
        if S[i:i+len(P)]==P:
            return 1
        if i+len(P)<len(S):
            i+=len(P)
        else:
            return 0

        
    return 0
print(solution(S,P))