# 문제풀이 :
#   다익스트라 알고리즘 활용.

# 1. 출발 노드를 설정한다.
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다. (갈 수 없는 경우 무한대로 초기화)
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
# 5. 위 과정에서 3~4번을 반복한다.

import sys
from heapq import heappush, heappop

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start)) # 시작지점 힙에 추가
    distance = [sys.maxsize] * (N + 1) # 각 정점사이의 거리 무한대로 초기화
    distance[start] = 0

    while heap:
        weight, index = heappop(heap)
        for e, c in bus[index]:
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heap, (weight + c, e))

    return distance[end]

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    bus[start].append((end, cost))

start, end = map(int, input().split())

print(dijkstra(start, end))