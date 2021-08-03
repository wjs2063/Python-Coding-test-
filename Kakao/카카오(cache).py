

cacheSize=2
cities=["Jeju", "Pangyo", "NewYork", "newyork"]

def solution(cacheSize, cities):
    cnt=0
    cache=[]
    # cache size 가 0이라면 그냥 all miss 임
    if cacheSize==0:
        return len(cities)*5

    for city in cities:
        city=city.lower()
        ## case1:cash hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            cnt+=1
            continue
            # 가장 최근에 사용되었으므로 마지막으로보낸다 list 뒤에있을수록 가장 최근에 사용한것임
        ## cache buffer 가 가득찼다면 LRU 기법으로 교체
        ## 하... 대소문자 구분 안한대 ㅡㅡ... 대소문자로 다바꿔주자
        if len(cache)==cacheSize:
            cache.pop(0)
            
            cache.append(city)

            cnt+=5
            continue
        cache.append(city)
        print(cache)
        cnt+=5
    answer=cnt

    return answer


            


    






print(solution(cacheSize,cities))