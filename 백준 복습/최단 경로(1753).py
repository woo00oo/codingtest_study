# heapq 라이브러리는 각 원소가 튜플일 경우에 첫번짜 인자 즉 (a, b)일 경우 a를 기준으로 최소힙을 구현한다.

from heapq import heappop, heappush

def dijkstra(start):
    distance[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        weight, node = heappop(heap)

        for end, w in graph[node]:
            if distance[end] > w + weight:
                distance[end] = w + weight
                heappush(heap, (w + weight, end))

V, E = map(int, input().split())
K = int(input())
graph = dict()
for i in range(1, V+1):
    graph[i] = []
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
distance = [float('INF') for _ in range(V+1)]
dijkstra(K)

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])