n=int(input())
f=[]
for i in range(n):
    f.append(str(input()))
string_length=len(f[0])


answer=""

for i in range(string_length):
    d=True
    for j in range(n):
        if j==n-1:
            break
        a=f[j][i]
        b=f[j+1][i]
        d= (d and (a==b))
    
    if d :
        answer+=f[j][i]
    else:
        answer+='?'
print(answer)
        