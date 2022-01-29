import bisect

a=[1,3,4,5,5,5,6,7]
print(a)
idx=bisect.bisect_left(a,4.5)
print(idx)
a[idx]=5
print(a)