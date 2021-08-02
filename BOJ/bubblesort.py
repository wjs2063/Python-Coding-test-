arr=[6,4,3,7,1,9,8]



def bubblesort(arr:list,n:int)->int:
    #오름차순
    count=0
    relate=0
    for i in range(n-1):
        for j in range(n-1,0,-1):
            if j>i:
                relate+=1
                if arr[j-1]>arr[j]:
                    temp=arr[j]
                    arr[j]=arr[j-1]
                    arr[j-1]=temp
                    count+=1
    
    for i in range(len(arr)):
        print(f'arr[{i}]={arr[i]}')
    return count,relate

a,b=bubblesort(arr,len(arr))

print("스왑횟수는 ",a,"비교횟수는",b)

