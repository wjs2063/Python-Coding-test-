# Big-Oh 표기법
""" 
O():Upper bound
오메가: Lower bound
빅세타: avarage
o():{x| O()에는 속하지만 not same degreeO()}
"""

# python 에서는 임의 정밀도를 지원한다.
""" 
임의정밀도란  한마디로 말해서 무제한 자릿수를 제공하는 정수형
가능한이유는 자릿수단위로 쪼개어 배열형태로 표현하기때문이다
"""

#mapping 
""" 
mapping type 은 key,data 로 구성된 복합자료형
파이썬에 내장된 유일한 mapping 자료형은 dictionary !
"""


#Set 

""" 
파이썬에서 빈 집합은 a=set() 로 표현
표현은 a={1,2,3}
dictionary 와 동일하게 {} 를 사용하지만 key:data 형태로 되어있지않아서 쉽게 구분가능

set은 입력순서가 유지되지않는다.
중복된값이 있으면 하나의값만 유지한다
합집합: a|b or set.union(a,b)
교집합: a&b or set.intersection(a,b)
차집합: a-b or set.difference(a,b)
대칭차집합: a^b or set.symmetric_difference(a,b)
부분집합: a.issubset(b) a가 b의 부분집합이면 True 반환 아니면 False
진부분집합:a<b a가 b의 진 부분집합이면 True반환
상위집합: a>=b a가 b의 상위집합(같아도됨)이면 True반환 a.issuperset(b)
겹치는 set가 겹치지않는지확인 : a.isdisjoint(b) a와 b의 교집합이 공집합이라면 True 겹치는게있으면 False
"""
from typing import SupportsIndex


a=set({"apple","banana","apple","abc"})
print(a)


#Sequence 

""" 
Sequence 는 불변과 가변으로 나뉜다
str 은 불변
list 는 가변
reason: a='abc' id('abc') 
"""
a='abc'
print(id(a))
print(id('abc'))
a='def'
print(id(a))
print(id("def"))
# 위실행 예제를 보면 a는 'abc'의 주소값을 참조하게되고 'def'의 주소값을 참조한다
#여기서 str 을 변경시키려면 a[1]='d' 를실행시켜보면 오류가 뜬다. 불변임을 알수있다.

# is 와 ==
""" 
is 는 id() 값을 비교하는 함수이다

a=[1,2,3]
a==a -> True
a==list(a) -> True
a is a -> True

a is list(a)-> False 별도의 객체로 복사가되고 다른 ID 를 갖게된다

즉 == 은 객체가 같은지 다른지 여부? 를 반환 하게되고 is 는 객체의 id 가같은지 반환하는 함수인것같다

a==copy.deepcopy(a) True
a is copy.deepcopy(a) False

"""

a=[1,2,3,4,5]
print(4 in a) # elem in a  a 라는 요소에 elem 가있는지 여부를 반환한다 bool 반환 ->bool

""" 
a.count(elem) a에 elem 가 몇개있는지 개수 return
a.index(elem) a 에 elem요소의 index return
a.append(elem) 리스트의 마지막에 elem 요소를 추가
a.pop() a라는 list 의 마지막 요소를 추출 스택
a.sort() Timsort 활용하여 정렬
a.reverse() list 를 뒤집는다
a.insert(m,n) m번째 index에 n을 삽입
"""
print(a[1:4:2])


try:
    print(a[9])
except IndexError:
    print("존재하지않는 index")

# del a[i] i번째 요소 삭제
#a.remove(x) x라는값 삭제
a=[1,1,1,2,3,4]
a.remove(1)
print(a) 
# 한개만 삭제됨 

for key,value in enumerate(a):
    print(f'({key},{value})')
    