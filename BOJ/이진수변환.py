import sys
input=sys.stdin.readline

n=int(input())
s=""
def binary(n):
    global s
    if n==0:
        return s+""
    n,r=divmod(n,2)
    binary(n)
    s+=str(r)
    return
binary(n)
print(s)