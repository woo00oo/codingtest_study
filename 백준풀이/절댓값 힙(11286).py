import heapq
import sys

heap = []
N = int(input())
for _ in range(N):
    number = int(sys.stdin.readline().strip())

    if number != 0:
        heapq.heappush(heap, (abs(number), number))
    else:
        try:
            answer = heapq.heappop(heap)[1]
            print(answer)
        except:
            print(0)
