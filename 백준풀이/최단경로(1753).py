# 다익스트라 알고리즘 활용.
# float('inf') -> 양의 무한대를 나타냄

from heapq import heappop, heappush

def dijkstra(start):
    distance = [float('inf') for _ in range(V+1)]
    distance[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        weight, node = heappop(heap)

        for end, w in graph[node]:
            if distance[end] > w + weight:
                distance[end] = w + weight
                heappush(heap, (w + weight, end))

    return distance


V, E = map(int, input().split())
K = int(input())
graph = dict()
for i in range(1, V+1):
    graph[i] = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # (도착지, 가중치)

answer = dijkstra(K)

for i in range(1, V+1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i])