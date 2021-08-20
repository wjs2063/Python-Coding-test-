
from itertools import permutations
user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["fr*d*", "*rodo", "******", "******"]

def solution(user_id, banned_id):
    def is_banned(users,banned_id):
        for i in range(len(banned_id)):
            #user list 의 각 index 의 길이가 다르면 확인할필요 x
            if len(users[i])!=len(banned_id[i]):
                return False
            #길이가 같다면 한개씩 check
            for j in range(len(users[i])):
                # 무시
                if banned_id[i][j]=='*':
                    continue
                if banned_id[i][j]!=users[i][j]:
                    return False
        return True

    user_ban_list=list(permutations(user_id,len(banned_id)))
    bans=[]
    for users in user_ban_list:
        if not is_banned(users,banned_id):
            continue
        else:

            users=set(users)
            if users not in bans:
                bans.append(users)
    return len(bans)
            
print(solution(user_id,banned_id))