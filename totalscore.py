score=[]
for i in range(8):
    score.append(int(input()))
copy=score
score.sort(reverse=True)
total=0
for i in range(5):
    total+=score[i]

print(total)



