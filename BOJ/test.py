def bubblesort(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

index=[5,4,3,2,1]

def quicksort(A,low,high):
    def partition(low,high):
        pivot=A[high]
        left=low
        for right in range(low,high):
            if A[right]<pivot:
                A[right],A[left]=A[right],A[left]
                left+=1
        A[left],A[high]=A[high],A[left]
        return left
    if low<high:
        pivot=partition(low,high)
        quicksort(A,low,pivot-1)
        quicksort(A,pivot+1,high)
