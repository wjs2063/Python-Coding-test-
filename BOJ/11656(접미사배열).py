strs=input()

r=[]

for i in range(len(strs)):
    r.append(strs[i:])
r.sort()
for i in range(len(r)):
    print(r[i])