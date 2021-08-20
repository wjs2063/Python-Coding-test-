def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2

    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        start=mid+1
        return binary_search(arr,target,start,end)
    if arr[mid]>target:
        end=mid-1
        return binary_search(arr,target,start,end)
    return None

def biserach(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            start=mid+1
            continue
        else:
            end=mid-1
    return None