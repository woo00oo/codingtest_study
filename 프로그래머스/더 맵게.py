# heap 자료구조를 사용 => 가장 작은 값, 가장 큰 값을 지속적으로 구해야할 경우 heapq라는 라이브러리를 사용하자
# heapq.heapify
# heapq.heappop
# heapq.heappush 와 같은 메소드가 존재하며, heapq는 최소힙으로 구현되어 있음 최대 힙을 사용하려면 트릭을 사용해야 함.
# 최대힙 => heapq를 사용하면서 해당 원소에 (-item, item) 의 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 됨.

import heapq

def solution(scoville,K):
    heapq.heapify(scoville)
    answer = 0

    while True:
        Min = heapq.heappop(scoville)
        if Min >= K:
            return answer
        if Min < K and len(scoville) == 0:
            return -1
        Min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, Min+(Min2*2))
        answer += 1
