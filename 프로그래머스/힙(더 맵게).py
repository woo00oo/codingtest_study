#리스트의 길이가 길 경우 sort메서드 사용시 효율성이 매우 떨어짐
#heapq라는 자료구조 사용
#push와 pop 메서드 호출시 자동으로 정렬 해주는 기능을 가짐



import heapq
def solution(scovile, K):
    answer = 0
    heap = []
    for num in scovile:
        heapq.heappush(heap,num)
    while(True):
        if K <= heap[0]:
            return answer
        elif len(heap) == 1 and heap[0] < K:
            return -1
        heapq.heappush(heap,heapq.heappop(heap)+(heapq.heappop(heap) * 2))
        answer += 1

print(solution([1,2,3,9,10,12],7))


