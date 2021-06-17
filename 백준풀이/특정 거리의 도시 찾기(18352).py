# 다익스트라 시간 복잡도 :
# 각 정점마다 인접한 간선들을 탐색하는 과정:
#   각 노드는 최대 한 번씩 방문하기 때문에 그래프의 모든 간선은 최대 한번씩 검사한다-> O(E)
# 우선순위 큐에 [거리, 정점] 정보를 넣고 빼는 과정
# 최악의 경우는 모든 간선을 검사할때 마다 거리 값 리스트가 갱신되고, 우선순위 큐에 정보가 저장되는 경우이다.
# E의 간선을 검사할 때 마다 우선순위 큐를 유지해야 하므로 이 과정의 시간복잡도는 O(ElogE)이다
# => O(ElogE)

# BFS 시간복잡도:
# 노드수 : V , 간선 수 : E
# O(V + E)

from collections import deque
import sys

def BFS(start, K):
    queue = deque()
    distance = [float("inf") for _ in range(N+1)]
    distance[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()

        for end in graph[node]:
            if distance[end] > distance[node] + 1:
                distance[end] = distance[node] + 1
                queue.append(end)

    answer = []
    for i in range(1, N+1):
        if distance[i] == K:
            answer.append(i)

    return answer



N, M, K, X = map(int, input().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

answer = BFS(X, K)
if len(answer) == 0:
    print(-1)
else:
    for city in answer:
        print(city)
