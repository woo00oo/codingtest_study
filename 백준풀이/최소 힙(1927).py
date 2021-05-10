import heapq
import sys

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) > 0:
            node = heapq.heappop(heap)
            print(node)
        else:
            print(0)
    else:
        heapq.heappush(heap, x)