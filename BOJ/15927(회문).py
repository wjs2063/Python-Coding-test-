from collections import Counter
a="AAAAAAAA"

# 모든 경우의 수를 생각해보자
# 길이가 1인 팰린드롬,2인 . . .n 인팰린드롬
# 길이가 1이면 그자체로 팰린드롬
# 길이가 2라면 aa 
# 길이가 3이라면 aba or aaa
# 길이가 4라면 abba or aaaa
# 길이가 5라면 abbba or aaaa or abcba 
# 문자를 몇개 썻는지 case 로 나눌수있겠다 
# 길이가 n=2k 라면 최대 k개의 문자
# 길이가 n=2k+1 라면 최대 k+1개의 문자
# 전체문자가 팰린드롬이라면 1개줄여보자 과연 이문자가 팰린드롬이 아닐까? 아니라는 보장은?
# n=2k 일떄 a1a2a3a4...akak...a4a3a2a1 나열해서 확인해보자
# 1개를 줄이면 중앙의 왼쪽 ak 가 center 가된다,팰린드롬이 이라면 ak=ak-1=ak-2..a1 가되는수밖에없음
# 따라서 모든문자가 같지않다면 팰린드롬이 아니다
# n=2k+1 이라면 a1a2a3a4...ak+1. . . a4a3a2a1 이다
# a1 을없앤결과가 팰린드롬이라면 이역시 a1=a2=a3=... ak+1 이되어야한다 
# origin 문자가 팰린드롬 이다? 그러면 모든문자가 같은지 check 같으면 -1 아니라면 len-1
# origin 문자가 팰린드롬이 아니라면? 그냥 그게답
if a==a[::-1]:
    if Counter(a)[a[0]]==len(a):
        print(-1)
    else:
        print(len(a)-1)
else:
    print(len(a))
print(Counter(a))