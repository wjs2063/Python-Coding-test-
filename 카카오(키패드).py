import numpy as np

def solution(numbers,hand):
    left=[1,4,7]
    right=[3,6,9]
    middle=[2,5,8,0]
    result=""
    leftcur="*"
    rightcur="#"
    pos=np.array([[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]],dtype=int)
    #pos->index 와 숫자위치가 같다고보면된다 예외는 10,11번쨰 pos[10]은 "*"을 pos[11]은 "#" 을나타낸다
    left_pos=pos[10]
    right_pos=pos[11]
    
    while len(numbers)!=0:
        dial=numbers.pop(0)
        if dial in left:
            
            left_pos=pos[dial]
            result+="L"
            continue
        if dial in right:
            right_pos=pos[dial]
            
            result+="R"
            continue
        if dial in middle:
            cur_pos=pos[dial]
            left_length=cur_pos-left_pos
            right_length=cur_pos-right_pos
            l_length=abs(left_length[0])+abs(left_length[1])
            r_length=abs(right_length[0])+abs(right_length[1])

            if r_length<l_length:
                right_pos=pos[dial]
                result+="R"
            elif l_length<r_length:
                left_pos=pos[dial]
                result+="L"
            else:
                if hand=="right":
                    right_pos=pos[dial]
                    result+="R"
                elif hand=="left":
                    left_pos=pos[dial]
                    result+="L"
        
    return result

a=solution([7,0,8,2,8,3,1,5,7,6,2],"left")
print(a)


