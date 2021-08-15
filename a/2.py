price=[78000, 48000, 27000, 285000, 320000, 335100]
def solution(price):
    money=int(1e8) # 순자산
    purpose=int(1e9) # 목표
    plus=int(5e7) # 5천만원 대출받을시
    cnt=0
    
    result=[]
    for i in range(len(price)-1):
        my_toss,rest=divmod(money,price[i])
        use_bank=False
        bank=0
        cnt=0
        for j in range(i+1,len(price)):
            print(i,j)
            print(my_toss,rest,bank,my_toss*price[j]+rest-bank,my_toss*price[j]+rest-bank>=purpose)
            cnt+=1
            # 차익실현 확인
            if my_toss*price[j]+rest-bank>=purpose:
                print(f'{i+1}번째날짜:차익실현{j+1}번쨰날짜 ')
                result.append(cnt)
                break
            # my_toss 는 대출후 최종주식 거기다 rest 까지더하면 순자산
            if price[j]<=price[i]/2 and not use_bank:
                use_bank=True
                bank+=plus
                plus_toss,rest=divmod(plus+rest,price[j])
                my_toss+=plus_toss
            
            if j==len(price)-1:
                result.append(-1)
            
    # 마지막날은 확인불가
    result.append(-1)
    return result
print(solution(price))