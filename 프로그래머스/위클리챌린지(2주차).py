scores=[[70,49,90],[68,50,38],[73,31,100]]
def solution(scores):
    answer = ''
    score_list=[]
    for i in range(len(scores)):
        student_score=[]
        for j in range(len(scores)):
            student_score.append(scores[j][i])
        max_val=max(student_score)
        min_val=min(student_score)
        if student_score[i]==max_val and student_score.count(max_val)==1:
            s=sum(student_score)-student_score[i]
            s/=len(student_score)-1
            score_list.append(s)
            continue
        if student_score[i]==min_val and student_score.count(min_val)==1:
            s=sum(student_score)-student_score[i]
            s/=len(student_score)-1
            score_list.append(s)
            continue
        s=sum(student_score)/len(student_score)
        score_list.append(s)
        print(score_list)
    
    for i in range(len(score_list)):
        if score_list[i]>=90:
            answer+='A'
            continue
        if score_list[i]>=80:
            answer+='B'
            continue
        if score_list[i]>=70:
            answer+='C'
            continue
        if score_list[i]>=50:
            answer+='D'
            continue
        else:
            answer+='F'
    return answer
print(solution(scores))