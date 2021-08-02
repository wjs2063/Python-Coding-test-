# indent
# 공식 가이드인 PEP(Python Enhancement Proposal)9을 따라 공백 4칸을 원칙
import pprint
"""  
foo=long_function_name(var_one,var_two,
                       var_three,var_four)
parameter 시작부분에 보기좋게 맞추기

def long_function(
        var_one,var_two,var_three
        var_four):
    print(var_one)
코드 첫번째 줄에 parameter 가없다면 공백 4칸 인덴트를 한번더 추가하여 다른행과 구분되게한다.


)




"""


# type hint 중요함

"""
a:str="1" a라는 변수는 str 자료형임을 a:str 로 나타내주고 a 에"1" 을 넣어준다라는 의미

함수부분에서는
def make_post(title:str,author_id:int=0)->str: 
이 의미는 make_post 함수는 parameter 를 title author_id 로 받아오는데 title=str 자료형 author_id는 int
형을 받아온다 그리고 이 함수의 반환값은 ->str 을 반환하다 라는 의미이다.가독성을 높이기위해 사용한다

def fn(a:int)->bool:
    a라는 parameter 는 int 형을 넣게될것이고 이 함수의 반환값은 bool 형태를 반환할것이라는 정보를 담고있다





"""
# list comprehension
print(map(lambda x:x+10,[1,2,3]))
print(list(map(lambda x:x+10,[1,2,3])))
print([n*2 for n in range(1,10+1) if n%2==1])
# map 함수는 map(lambda x:f(x),[정의역]) lambda 로 정의된 함수를 다 적용시켜준후 값을 반환해준다
# filter 함수는 filter(함수,적용시킬요소들)
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,8.2])))

# dictionary version 2.7 이후 다음과 같이 list 이외에 dictionary 등이 가능하도록 추가됐다.
a={"최윤지":26,
   "전재현":27}
print(a)

b={key:value for key,value in a.items()}
for i in range(5):
    print(i,end=" finish ")

"""
a=[n for in range(100000)]
n=range(100000)
의 차이점은 메모리점유율 차이
len(a) == len(b) True 가 나온다 
차이점은 a는 이미 생성된 값이 담겨있고 b 는 생성해야한다는 조건이담겨있다

메모리점유율은 sys.getsizeof(a) sys.getsizeof(b) 를 해보면 나온다
미리생성하지않은값은 인덱스접근이 가능하다 . 인덱스접근시 바로생성하도록 구현이되어있다.
"""


#enumerate() 
"""
열거하다라는 의미  list,set,tuple 을 인덱스를 포함한 enumerate 객체로 반환한다
ex) a=['a1','b1','c1']
인덱스와 값을 동시에 출력하려면?

for i in range(len(a)):
    print(i,a[i])
a[i] 조회작업과 전체길이 조회 loop 처리형태가 깔끔하지않다

i=0
for v in a :
    print(i,v)
    i+=1
인덱스를 위한 변수를 별도로 관리하여 깔끔x

for i,v in enumerate(a):
    print(i,v)
가장 깔끔한 형태


"""


#나눗셈 연산자

# 몫과 나머지를 한번에 구할때 divmod(5,3)=(몫,나머지) 형태로 tuple 형태로반환

print(type(divmod(5,3)))

print('A1','B2',sep=',')
# sep=구분자로서 ',' A1과B1을 로 구분해준다

# list 출력할때에는 join()로 묶어서 출력

a=['A','B']
print(a)
print(' '.join(a))

# f-string python 3.6 이상에서만 지원한다!
idx=0
fruit="Apple"
print(f'{idx+1}:{fruit}')

# pass 기능

"""

"""
#import pprint 
#pprint.pprint(locals()) class method 내부의 모든 local 변수를 출력해주기 때문에 debugging 에도움된다
pprint.pprint(locals())

# find 함수 문자열이없을시 -1 return, index 함수 문자열이없을시 오류

a=[(x,y,z)
   for x in range(5)
   for y in range(5)
   if x !=y
   for z in range(5)
   if y!=z]
print(a)
print("0<=x,y,z<=4 인 정수이며 x!=y 이고 y!=z 인 순서쌍들의집합 ")
