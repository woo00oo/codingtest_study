# 첫번째 시도 :
#   최대힙과 , 최소힙 두개 힙을 만들어 해결. => 시간 초과
#   최대힙과 최소힙의 동기화를 위해 remove 메소드 사용 -> remove() O(N)이라는 시간복잡도를 가짐



import heapq
import sys

# T = int(input())
# for _ in range(T):
#     max_heap = []
#     min_heap = []
#     k = int(input())
#     for _ in range(k):
#         op = sys.stdin.readline().strip()
#         if 'I ' in op:
#             op = op.replace('I ', '')
#             op = int(op)
#             heapq.heappush(max_heap, (-op, op))
#             heapq.heappush(min_heap, op)
#         elif 'D -1' == op:
#             if len(min_heap) > 0:
#                 node = heapq.heappop(min_heap)
#                 max_heap.remove((-node, node))
#         elif 'D 1' == op:
#             if len(max_heap) > 0:
#                 node = heapq.heappop(max_heap)[1]
#                 min_heap.remove(node)
#
#     if len(max_heap) > 0 and len(min_heap) > 0:
#         max_num = heapq.heappop(max_heap)[1]
#         min_num = heapq.heappop(min_heap)
#         print(max_num, min_num)
#     else:
#         print("EMPTY")


# heapq.nlargest(n, list) 함수를 사용하면 list에서 가장 큰 n개의 수를 뽑아낼 수 있다.

T = int(input())
for _ in range(T):
    heap = []
    k = int(input())
    for _ in range(k):
        op = sys.stdin.readline().strip()
        if 'I ' in op:
            op = op.replace('I ', '')
            op = int(op)
            heapq.heappush(heap, op)
        elif 'D -1' == op:
            if len(heap) > 0:
                heapq.heappop(heap)
        elif 'D 1' == op:
            if len(heap) > 0:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if len(heap) > 0:
        max_num = heapq.nlargest(len(heap), heap)[0]
        min_num = heapq.heappop(heap)
        print(max_num, min_num)
    else:
        print("EMPTY")