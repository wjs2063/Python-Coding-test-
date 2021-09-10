def binary(a,start,end,target):
    mid=(start+end)//2
    if start>end:
        return 0
    if a[mid]==target:
        return 1
    if a[mid]<target:
        return binary(a,mid+1,end,target)
    return binary(a,start,mid-1,target)

    


n=input()
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))
for x in b:
    print(binary(a,0,len(a)-1,x))

