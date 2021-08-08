left,right=map(str,input().split(" ",1))
# Left,right중 8이 없는애가 존재한다면 0을 준다
#역시 시간초과 ^^
'''
def solution(left,right):
    # 8이 없는애가 존재하면 그냥 return 0 
    if left.count("8")<1 or right.count("8")<1:
        return 0
    min_left=left.count("8")
    left=int(left)
    right=int(right)
    while left<right:
        if str(left).count("8")<min_left:
            min_left=str(left).count("8")
        left+=1
    return min_left
print(solution(left,right))
'''

def solution(left,right):
    if left==right:
        return left.count("8")
    # 8이 없는게 있다면 그냥 0
    if left.count("8")<1 or right.count("8")<1:
        return 0
    # 길이가 다르면 무조건 0
    if len(left)!=len(right):
        return 0
    # 길이가 같다면
    # 순차비교
    left=list(left)
    right=list(right)
    cnt=0
    
    for i in range(len(left)):
        # 예를들어 8788, 8888 을 보자 
        #  i번째가 달라졌다면 그뒤로는 볼필요가없게됨
        # i번째가 숫자가 다르다면 그뒤로는 무조건 8이없게 만들수있게된다
        if left[i]!=right[i] :
            break
        # 둘다 8이라면 바뀔수없는것 그 자리는 바뀔수없다. 
        if left[i]==right[i] and left[i]=="8":
            cnt+=1

    return cnt

print(solution(left,right))

    

    