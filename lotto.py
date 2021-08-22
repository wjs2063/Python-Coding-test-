import requests

from bs4 import BeautifulSoup
import bs4
import urllib.request
import numpy as np 
import re
import sys
print(requests.__version__)
print(bs4.__version__)
print(np.__version__)
address=requests.get("https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1")

soup=BeautifulSoup(address.text,'html.parser')  ## html 의 내용을 bs 모듈한테 건네준다

## 홈페이지의 tag class 확인하기
## 개발자 도구를 클릭해서 확인해보니 class=num win 이고 div 태그 와  span 이다 
first=soup.find('div',class_='num win')
second=first.find_all('span') # second에 span 과 관련된 모든것이 저장되어있다.
#num_win 과 관련된 것 들 -> span 에 해당되는부분

print(second) #print 를 하면 
print(second[0].text) ## 첫번째 번호가나오는것을 확인할수있다

for target in second:#second 에저장되어있는 span 부분의 text 만 반복 프린트
    print(target.text)

bonus=soup.find('div',class_='num bonus')# class 가 num bonus 고 tag가 div인 html내용을 bonus에 저장
bonusnumber=bonus.span.text #bonus안의 html내용중 span태그의 text를 저장
print("Bonus number==",bonusnumber)

finallist=[]
def nthnumber(n,list=finallist):
    list.append(n)
    for target in second:
        list.append(int(target.text))# list 저장
    
    bonus=soup.find('div',class_='num bonus')
    bonusnumber=bonus.span.text
    list.append(int(bonusnumber))
# 나중에 수식연산을 할수도있으니 
for n in range(1,15): # 숫자를 너무크게하면 시간너무오래걸려서 안나옴 적당히 1~n까지로 하자..
    page="https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="+str(n)
    tes=requests.get(page)
    soup=BeautifulSoup(tes.text,'html.parser')
    soup2=soup.find('div',class_='num win')
    final=soup2.find_all('span')
    finallist.append(int("{}".format(n)))
    for index in final:
        finallist.append(int(index.text))
    bonus=soup.find('div',class_='num bonus')
    bonusnumber=bonus.span.text
    finallist.append(int(bonusnumber))
    
finallist=np.array(finallist).reshape(14,8) # 보기좋게 14행 8열 (회차+로또번호개수(7개))총 8개다 보너스는 마지막
#추후에 머신러닝 다음 로또번호 예측해볼것임.

print(finallist)