path=[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order=[[8,5],[6,7],[4,1]]
n=9
from collections import deque
def solution(n, path, order):
    answer = True
    graph=[[] for _ in range(n)]
    visited=[False for _ in range(n)]
    for p1,p2 in path:
        graph[p1].append(p2)
        graph[p2].append(p1)
    before=[ 0 for _ in range(n)]
    cnt=0
    # before 
    for prev,next in order:
        before[next]=prev
    q=deque([0])
    have_to={}
    while q:
        v=q.popleft()
        # v에 대하여 v 를 갈떄 이전에 들러야할 곳이있나요?
        if before[v] and not visited[before[v]]:
            # 네 있습니다
            # 그러면 have_to 에 before[v]에 v 를 넣으세요
            have_to[before[v]]=v
            continue
        # 이전에 들러야할곳이 없으면
        visited[v]=True
        cnt+=1
        # 현재 vertex 와 연결되어있는 곳 을 가보자
        for vertex in graph[v]:
            if not visited[vertex]:
                q.append(vertex)
        # 방문한점이 have_to 에있으면
        # 이제는 방문가능
        if v in have_to:
            q.append(have_to[v])
    return cnt==n

print(solution(n,path,order))


    
