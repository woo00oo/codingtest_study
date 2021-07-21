# 다익스트라 알고리즘 활용.

import heapq

def dijkstra(N, graph):
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        weight, node = heapq.heappop(heap)

        for w, end_node in graph[node]:
            if distance[end_node] > w + weight:
                distance[end_node] = w + weight
                heapq.heappush(heap, (w + weight, end_node))

    return distance

def solution(N, road, K):
    answer = 0
    graph = dict()

    for i in range(1, N+1):
        graph[i] = []

    for n1, n2, w in road:
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    distance = dijkstra(N, graph)

    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer
