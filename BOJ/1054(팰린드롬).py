

n=int(input())
word_list=[]
for i in range(n):
    word_list.append(input())

##메모리 초과가 나는 문제이므로 generator 활용?
def solutions(arr,r):
    result=[]
    # nPr 에서 r이 n보다 클순없으니까
    if r>len(arr):
        return result
    if r==1:
        for element in arr:
            result.append([element])
    if r>1:
        for i in range(len(arr)):
            temp_word=arr[:]
            temp_word.remove(arr[i])
            # i번째 요소를 빼준다
            #그리고 answer에 추가
            for p in solutions(temp_word,r-1):
                if len(p)==r-1:
                    yield [temp_word[i]]+p


print(next(solutions(word_list,1)))
    




            


 
