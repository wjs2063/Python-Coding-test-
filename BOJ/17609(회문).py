import sys
import re
from collections import deque
input=sys.stdin.readline
n=int(input())

def check(x,left,right):
    while left<right:
        if x[left]==x[right]:
            left+=1
            right-=1
            continue
        return False
    return True


def palindrome(x):
    if x==x[::-1]:
        return 0
    left,right=0,len(x)-1
    while left<right:
        if x[left]==x[right]:
            left+=1
            right-=1
            continue
        c1=check(x,left+1,right)
        c2=check(x,left,right-1)
        
        if c1|c2:
            return 1
        break
    return 2



for _ in range(n):
    strs=input().rstrip()
    print(palindrome(strs))