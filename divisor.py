number=int(input())
a=list(map(int,input().split()))
a.sort()
print(a)
n=len(a)%2
q=len(a)//2
result=1
if n==0:
    # n이 짝수면
    result=a[0]*a[-1]
else :
    result=a[q]*a[q]

print(result)
    