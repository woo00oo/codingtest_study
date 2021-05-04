# 힙을 두개 사용하여 풀이, 최대힙과 최소힙을 따로 두어 처리 하였다.
# 하지만 최소 힙에서 최대값을 삭제할 수 있는 방법도 존재한다.
# heap = heapq.nlargest(len(heap), heap)[1:]
# heapq.heapify(heap)
# -> heapq.nlargest(n, list) 함수를 사용하면 list에서 가장 큰 n개의 수를 뽑아낼 수 있다.
# 위 코드에서는 heap의 원소 개수만큼 뽑아내기 때문에 전체 heap 리스트가 내림차순으로 정렬된다.
# 그 후 인덱스 1부터 슬라이싱하면 가장 큰 최대값이 제외될 것이고, 다시 최소힙으로 만들어주면 된다.


import heapq

def solution(operations):
    max_heap = []
    min_heap = []

    for op in range(len(operations)):
        if 'I ' in operations[op]:
            operations[op] = operations[op].replace('I ', '')
            number = int(operations[op])
            heapq.heappush(max_heap, (-number, number))
            heapq.heappush(min_heap, number)

        elif 'D -1' == operations[op]:
            if len(min_heap) > 0:
                num = heapq.heappop(min_heap)
                max_heap.remove((-num,num))
        else:
            if len(max_heap) > 0:
                num = heapq.heappop(max_heap)
                min_heap.remove(num[1])

    if min_heap:
        return [heapq.heappop(max_heap)[1],heapq.heappop(min_heap)]
    else:
        return [0, 0]

