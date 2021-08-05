# cache의 인덱스 번호가 낮을 수록 캐시 참조가 오래 되었다는 의미 => LRU 알고리즘에 의해 인덱스 번호가 가장 낮은 데이터를 pop

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize != 0:
        for city in cities:
            city = city.lower()
            # 캐시 hit일 경우
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            # 캐시 miss일 경우
            else:
                # 캐시에 자리가 없을 경우
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(city)
                answer += 5
    else:
        answer += len(cities) * 5

    return answer

'''
캐시 사이즈가 0일 경우와 0이 아닐 경우로 나눠서 생각하자.

'''