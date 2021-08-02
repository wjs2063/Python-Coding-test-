n=int(input())
string_list=[]
length_list=[]
counting_alphabet=""
for i in range(n):
    string_list.append(str(input().rstrip()))
    
    counting_alphabet+=string_list[i]
    
k=int(input())


change=[i for i in range(36)]



def full_adder(difference:list,sum)->str:
    
    s=""
    if k==0:
        if sum==0:
            return str(0)
        while sum!=0:
            
            rest=sum%36
            s+=translate_str(rest)
            sum=sum//36
    
        return s
        

    for i in range(k):
        sum+=difference[i]
        
    
    
    
    while sum!=0:
        
        rest=sum%36
        s+=translate_str(rest)
        sum=sum//36
    
    return s

def half_adder(string_list:list,change)->list:
    df=[]
    
    for j in range(36) :   
        sum=0
        
        
        for word in string_list:
            t=word.replace(change[j],'Z')
            # Z 로 바뀐 문자열 t 와 바뀌지않은 word  그것들의 10진수 의 차이
            sum+=(summation(t)-summation(word))
            
        df.append(sum)
    return df




def translate_number(a:str)->int :
    if 48<=ord(a)<=57:
        return ord(a)-48
    elif 65<=ord(a)<=90:
        return ord(a)-55
    return -1

def translate_str(a:int)->str:
    if 0<=a<=9:
        return chr(a+48)
    elif 10<=a<=35:
        return chr(a+55)

    return ""

def summation(a:str)->int:
    sum=0
    for i in range(len(a)):
        sum+=translate_number(a[-(i+1)])*(36**i)
    
    return sum
        

for i in range (36):
    change[i]=translate_str(change[i])


#알파벳 순서대로 'A'를 Z로 바꾼후 그 합을 계산 list 저장






counting_alphabet=set(counting_alphabet)
if len(counting_alphabet)<=k:
    difference=[]
    b=[]
    for s in string_list:
        a=""
        for j in range(len(s)):
            a+='Z'
        
        b.append(a)    
    difference=half_adder(b,change)
    difference.sort(reverse=True)

    sum=0
    for i in range(n):
        sum+=summation(b[i])
    
    print(full_adder(difference,sum)[::-1])
else :
    a=string_list[:]
    difference=half_adder(a,change)
    difference.sort(reverse=True)

    sum=0
    for i in range(n):
        sum+=summation(string_list[i])

    print(full_adder(difference,sum)[::-1])



