origin_word=input()

#역으로 바꿔준후
word=origin_word[::-1]

length=0
pos=0
if origin_word==word:
    print(len(word))

else :
    for i in range(len(word)):
        
        origin=word[pos:pos+i]
        #revers 한거
        reverse=origin[::-1]
        if origin==reverse:
            # 팰린드롬이라면
            #길이저장
            length=max(i,length)
    #기본적으로 최대 2*len(word) 길이만큼 만들수있다 (주어진거 그대로 거꾸로 복붙)
    #주어진단어의 역순으로 팰린드롬을 검출해서 그길이만큼 절약시킨다고보면됨. 
    print(2*len(word)-length)
    
