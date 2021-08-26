n=int(input())
apartment=[]
for _ in range(n):
    s=list(input())
    s=list(map(int,s))
    apartment.append(s)
cnt=0
visited=[[False]*n for _ in range(n)]
#visited 만들어주기
cnt=0

def dfs(x,y):
    global cnt
    # cnt=0 을했을때 안된이유
    # 매 함수실행마다 지역변수 cnt=0 으로 초기화를 해서 결국 0+0+0+ 꼴이되어버림
    if x<0 or x>=n or y<0 or y>=n or apartment[x][y]==0:
        return 0
    if visited[x][y]:
        return 0
    apartment[x][y]=0
    cnt+=1
    visited[x][y]=True

    # 상
    dfs(x-1,y)
    # 하
    dfs(x+1,y)
    # 좌
    dfs(x,y-1)
    # 우
    dfs(x,y+1)

    return cnt
result=0
answer=[]
for i in range(n):
    for j in range(n):
        cnt=0
        a=dfs(i,j)
        if a!=0:
            result+=1
            answer.append(a)
print(result)
answer.sort()
for x in answer:
    print(x)


