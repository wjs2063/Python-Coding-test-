strs=input().split('-')
# 문자 아닌것들을 기준으로 다 나눠주기 문제조건에 의해
# 03 과같은것들 3으로만들어주기
total=[]
for i in range(len(strs)):
    t=0
    a=strs[i].split('+')
    if len(a)>1:
        for j in range(len(a)):
            t+=int(a[j])
        total.append(t)
        continue
    total.append(int(a[0]))

total=-sum(total)+2*total[0]
print(total)
# -를 기준으로 다 나누기
# + 먼저 해주고 다 뺴면 값이 작아질테니까
# 아니 왜 syntax error 뜨냐고
# eval 쓰지말것 syntax 오류남
