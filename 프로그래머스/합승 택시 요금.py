'''
최단 거리를 구하기 위해 다익스트라 알고리즘 활용.

A와 B가 헤어지는 지점을 K라고 하면 => 요금 = 다익스트라(출발점, K) + 다익스트라(K, A의 도착지점) + 다익스트라(K, B의 도착지점)

주어진 모든 지점을 하나씩 K에 대입하여 나온 요금들 중 가장 작은 값이 정답.

'''
from heapq import heappush, heappop


def dijkstra(start_node, end_node, graph, n):
    heap = []
    heappush(heap, (0, start_node))
    distance = [float('inf') for _ in range(n+1)]
    distance[start_node] = 0

    while heap:
        w, node = heappop(heap)

        # 해당 노드를 방문하는데 드는 비용이 기존 최소비용보다 큰 경우는 무시
        # 이 코드를 생략할 경우 효율성에서 시간초과가 발생.(즉, 이미 값이 커지면 방문할 필요가 없는데 불필요한 연산을 계산하게 됨)
        if distance[node] < w:
            continue

        for weight, next_node in graph[node]:
            if distance[next_node] > w + weight:
                distance[next_node] = w + weight
                heappush(heap, (w+weight, next_node))

    return distance[end_node]


def solution(n, s, a, b, fares):
    answer = float('inf')

    # 그래프 구성
    graph = dict()
    for i in range(1, n+1):
        graph[i] = []

    for i in range(len(fares)):
        start, end, f = fares[i]
        graph[start].append((f, end))
        graph[end].append((f, start))

    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i, graph, n) + dijkstra(i, a, graph, n) + dijkstra(i, b, graph, n))

    return answer

