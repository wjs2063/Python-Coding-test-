n=int(input())
A,B,C,D,E,F=map(int,input().split())

dice=[[B,C,D,E],
       [A,C,D,F],
       [A,B,E,F],
       [A,B,E,F],
       [A,C,D,F],
       [B,C,D,E]]
first=[A,B,C,D,E,F]
dia=[(A,F),(B,E),(C,D)]
# 3면 합 최대 
three=999999999999
for i in range(6):
    if first[i] in dia[0]:
        x1=first[i]+dia[1][0]+dia[2][0]
        x2=first[i]+dia[1][0]+dia[2][1]
        x3=first[i]+dia[1][1]+dia[2][0]
        x4=first[i]+dia[1][1]+dia[2][1]
        three=min(x1,x2,x3,x4,three)
    elif first[i] in dia[1]:
        x1=first[i]+dia[0][0]+dia[2][0]
        x2=first[i]+dia[0][0]+dia[2][1]
        x3=first[i]+dia[0][1]+dia[2][0]
        x4=first[i]+dia[0][1]+dia[2][1]
        three=min(x1,x2,x3,x4,three)
    else:
        x1=first[i]+dia[0][0]+dia[1][0]
        x2=first[i]+dia[0][0]+dia[1][1]
        x3=first[i]+dia[0][1]+dia[1][0]
        x4=first[i]+dia[0][1]+dia[1][1]
        three=min(x1,x2,x3,x4,three)
        
   
            


# 2면 합 최대

two=99999999999999
for i in range(6):
    
    for j in range(4):
        total=dice[i][j]+first[i]
        two=min(two,total)
            


# 1면 합 최대
# 그냥 주사위 면

# n==1 일때 그냥 주사위 5면 최댓값

# n==2 일때 three*4 +two*4

# n>= 3일때  1면 (n-2)**2+4(n-1)(n-2) 2면 8n-12 3면 4
print(two,three)
if n==1:
    a1=B+C+D+E+F # A 가없
    a2=A+C+D+E+F # B가 없
    a3=A+B+D+E+F
    a4=A+B+C+E+F
    a5=A+B+C+D+F
    a6=A+B+C+D+E
    answer=min(a1,a2,a3,a4,a5,a6)
    print(answer)

elif n==2:
    answer=two*4+three*4
    
    print(answer)
    

else:
    one=min(A,B,C,D,E,F)
    answer=one*((n-2)**2+4*(n-1)*(n-2))+two*(8*n-12)+three*4
    print(answer)





