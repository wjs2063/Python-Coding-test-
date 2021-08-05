



def pellindrom(word):
    def wide(word,left,right):
        ''' left>=0 right<=len 인건 자명하다
        word[left]==word[right-1]은 1,3,5...or 2,4,6...인 case 에대해
        길이가 홀수케이스라면 right -> 2,4,6 씩 
        길이가 짝수케이스라면 left ->1,3,5 씩 
        '''
        while left>=0 and right<=len(word) and word[left]==word[right-1]:
            left-=1
            right+=1 
            # 확장 시키기  left 와 right-1 이 같아면
        return word[left+1:right-1]
    # 왜 left +1,right-1 이냐면 ++ or -- 를 진행후 조건 검사에 부적합하면 빠져나온다 그경우를 생각하면된다
    
    if len(word)<2 or word==word[::-1]:
        return len(word)
    answer=""
    for i in range(len(word)-1):
        answer=max(answer,
                    wide(word,i,i+1),
                    wide(word,i,i+2),
                    key=len)
    s=len(answer)
    return s
