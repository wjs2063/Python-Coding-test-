from itertools import permutations
cards=["LLZKE", "LCXEA","CVPPS","EAVSR","FXPFP"]
word='APPLE'
permute=[str(i) for i in range(len(word))]
word_len=len(word)
card_len=len(cards)
possible=[[] for _ in range(word_len)]
for i in range(word_len):
    for x in range(card_len):
        for y in range(card_len):
            if cards[x][y]==word[i]:
                possible[i].append((x,y))
# 각 단어가 있을수있는 위치들을 저장
length_list=[len(possible[i]) for i in range(word_len)]
result=0
# 길이저장
try:
    for i in range(length_list[0]):
        for j in range(length_list[1]):
            for k in range(length_list[2]):
                for m in range(length_list[3]):
                    for t in range(length_list[4]):
                        for l in range(length_list[5]):
                            for l1 in range(length_list[6]):
                                for l2 in range(length_list[7]):
                                    a=zip(length_list[0][i],length_list[1][j],length_list[2][k],length_list[3][m],length_list[4][t],length_list[5][l],length_list[6][l1],length_list[7][l2])
                                    a0=set(a[0])
                                    a1=set(a[1])
                                    a=[i for i in range(len(cards))]
                                    a=set(a)
                                    if a0==a1==a:
                                        result+=1
except:


