strings=["sun","bed","car","abce",'abcd']
def solution(strings,n):
    answer=[]
    index=[]


    for i in range(len(strings)):
        index.append(strings[i][n])
    sorted_index=sorted(index)
    index_number=[]
    for i in range(len(strings)):
        for j in range(len(strings)):
            if sorted_index[i]==index[j]:
                index_number.append(j)
    

    for i in index_number:
        answer.append(strings[i])
    
    return answer

strings.sort(key=lambda x:x[1])
print(strings)
