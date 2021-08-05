def solution(s):
    answer =len(s)


    for i in range(1,len(s)//2+1):
        # i는 문자열 parsing 
        # pos 는 위치 
        l=len(s)
        pos=0

        while pos+i<=len(s):
            strs=s[pos:pos+i]
            pos+=i # parsing 단위만큼 읽어왔으므로 증가시킴
            count=0
            while pos+i<=len(s):
                # 위치 증분시키고난다음 
                if strs==s[pos:pos+i]:
                    count+=1
                    pos+=i
                else :
                    break
            # 반복이 있었다면?
            if count>=1:
                l-=i*count
                # 1자리는 상관 +1 2자리는 +2개 3자리는 +3개 
                if count<9:
                    l+=1
                elif count<99:
                    l+=2
                elif count<999:
                    l+=3
                else :
                    l+=4
            if l<answer:
                answer=l

    return answer