key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate():
    # len(key)차원 value
    n=len(key) 
    r=[[0]*n for _ in range(n)]
    for k in range(n-1,-1,-1):
        for i in range(n):
            r[i][k]=key[n-1-k][i]
    return r
# key 의 size m x m 
# lock 의 size n x n 
# m+n-2 사이즈의 큰 array 생성후 sliding
# 
def big(key,lock):
    r=len(key)
    c=len(lock)
    for i in range(c):
        lock[i]=[2]*(r-1)+lock[i]+[2]*(r-1)
    



def solution(key, lock):
    answer = True
    while True:

    return answer