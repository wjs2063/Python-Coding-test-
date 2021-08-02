t=int(input())
testcase=[]

def fibo(testcase,count_test,n):
    if n==0:
        print(count_test[0][0],count_test[0][1])
        return
    if n==1:
        print(count_test[1][0],count_test[1][1])
        return

    for i in range(2,n+1):
        n_1=count_test[i-1][0]
        n_2=count_test[i-2][0]
        n_th=n_1+n_2
        k_1=count_test[i-1][1]
        k_2=count_test[i-2][1]
        k_th=k_1+k_2
        count_test.append([n_th,k_th])
    return count_test

        







for i in range(t):
    testcase.append(int(input()))
count_test=[[1,0],[0,1]]

max_number=max(testcase)

answer=fibo(testcase,count_test,max_number)
i=0
while len(testcase):
    a=testcase.pop(0)
    print(answer[a][0],answer[a][1])
    



    

    
