from heapq import heappush, heappop


def dijkstra(start_node):
    heap = []
    distance = [float('inf')] * (N+1)
    distance[start_node] = 0
    heappush(heap, (0, start_node))

    while heap:
        weight, node = heappop(heap)

        for w, end in graph[node]:
            if distance[end] > weight + w:
                distance[end] = weight + w
                heappush(heap, (weight+w, end))

    return distance


# 입력
N, V = map(int, input().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []

for _ in range(V):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

start = int(input())
distance = dijkstra(start)

# 출력
for idx, dis in enumerate(distance):
    if idx == 0:
        continue

    print(idx, end='')
    print(': ', end='')
    print(dis)

'''

다음과 같이 format 메소드를 사용하여 간략하게 처리가 가능하다.

for index,i in enumerate(answer):

	print("{0}: {1}".format(index+1,i))


'''