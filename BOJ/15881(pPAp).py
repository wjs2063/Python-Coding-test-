n=int(input())
strs=input()
pos=0
size=4
cnt=0
while pos+size-1<len(strs):
    if strs[pos:pos+size]=="pPAp":
        cnt+=1
        pos+=3
    pos+=1
print(cnt)
