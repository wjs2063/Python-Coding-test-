
x,y=map(int,input().split())

p=int((100*y)/x)

originprob=p
prob=originprob


if prob>=99:
    print(-1)

else:
    i=int(((p+1)*x-100*y)/(99-p))
    prob=int(100*(y+i)/(x+i))
    count=i
    while prob==originprob:
        i+=1
        count=i
        prob=int((100*(y+i))/(x+i))
    print(count)




