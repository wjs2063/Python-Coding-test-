n=int(input())
score=list(map(int,input().split()))
max_score=max(score)
a=lambda x: x/max_score*100
score=list(map(a,score))
print(sum(score)/n)